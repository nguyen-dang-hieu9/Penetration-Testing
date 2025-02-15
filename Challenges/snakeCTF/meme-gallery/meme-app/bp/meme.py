from . import blueprint
from utils import token_required, bucket_for, with_db
from utils import BOT_ADDRESS
from flask import request, render_template, Response, current_app
import mimeparse
from random import choice
import requests
from urllib.parse import quote_plus

ct_whitelist = [("image", "jpeg"), ("image", "png")]
ext_whitelist = [".png", ".jpeg", ".jpg"]


@blueprint.route("/upload", methods=["GET"])
@token_required
def upload_page(_):
    return render_template("upload.html", page_title="Share the fun", action="Upload")


@blueprint.route("/upload", methods=["POST"])
@token_required
@with_db
def upload(db, user):
    bucket = bucket_for(user)
    file = request.files["file"]

    if file.filename is None:
        return {"error": "Invalid meme"}, 400

    exts = map(lambda x: file.filename.endswith(x), ext_whitelist)
    if not any(exts):
        return {"error": "Invalid extension"}, 400

    objs = db.bucket_memes(bucket)
    if file.filename in objs:
        return {"error": "Meme exists"}, 400

    content = file.stream.read()
    content_type = mimeparse.parse_mime_type(file.content_type)
    if len(content_type) != 3:
        return {"error": "Invalid Content-Type"}, 400
    cts = map(
        lambda x: x[0] == content_type[0]
        and x[1] == content_type[1]
        and content_type[2] == {},
        ct_whitelist,
    )
    if not any(cts):
        return {"error": "Content-Type not allowed!"}, 400

    db.add_meme(file.filename, content, file.content_type, user.id, bucket)
    db.commit()

    return {"message": "Uploaded!"}, 200


@blueprint.route("/random", methods=["GET"])
@with_db
def random(db):
    bucket = "memes"

    memes = db.bucket_memes(bucket)
    res = choice(memes)
    o = db.retrieve_meme_data(res, bucket)

    return Response(o.stream(), o.status, o.headers.items())


@blueprint.route("/list", methods=["GET"])
@token_required
@with_db
def list_memes(db, user):
    bucket = bucket_for(user)
    meme = db.bucket_memes(bucket)[0]

    return {}, 302, {"Location": f"/list/{quote_plus(meme)}"}


@blueprint.route("/list/<meme>", methods=["GET"])
@token_required
@with_db
def view_meme(db, user, meme):
    bucket = bucket_for(user)
    memes = db.bucket_memes(bucket)
    if meme not in memes:
        return {}, 302, {"Location": "/list"}

    idx = memes.index(meme)
    next = memes[(idx + 1) % len(memes)]
    prev = memes[(idx - 1) % len(memes)]

    comments = db.find_comments(meme, bucket)

    return render_template(
        "list.html",
        page_title="This one is funny",
        meme=meme,
        next=next,
        prev=prev,
        comments=comments,
    )


@blueprint.route("/get/<meme>", methods=["GET"])
@token_required
@with_db
def get_object(db, user, meme):
    bucket = bucket_for(user)
    found = db.find_meme(meme, bucket)
    if found is None:
        return {"error": "Meme not found!"}, 404
    o = db.retrieve_meme_data(meme, bucket)

    return Response(o.stream(), o.status, o.headers.items())


@blueprint.route("/delete/<meme>", methods=["POST"])
@token_required
@with_db
def delete(db, user, meme):
    bucket = bucket_for(user)
    found = db.find_meme(meme, bucket)
    if found is None:
        return {"error": "Meme not found!"}, 404
    if found[2] != user.id:
        return {"error": "Not your meme!"}, 400
    db.delete_meme(meme, bucket)
    db.commit()

    return {}, 302, {"Location": "/list"}


@blueprint.route("/comment/<meme>", methods=["POST"])
@token_required
@with_db
def add_comment(db, user, meme):
    bucket = bucket_for(user)

    data = request.form
    if not data or "comment" not in data:
        return {"error": "No comment given"}, 400
    comment = data["comment"]

    found = db.find_meme(meme, bucket)
    if found is None:
        return {"error": "Meme not found!"}, 404
    meme_id = found[0]
    db.add_comment(comment, user.id, meme_id)
    db.commit()

    return {}, 302, {"Location": f"/list/{quote_plus(meme)}"}


@blueprint.route("/list/<meme>/maketheadminlaugh", methods=["GET"])
@token_required
@with_db
def report(db, user, meme):
    bucket = "supermemes"

    found = db.meme_bucket(meme)
    if found is None:
        return {"error": "Nonexistent meme is the new meme"}, 404
    if found != bucket:
        return {"error": "I'm not interested in this naive memes"}, 400
    res = requests.post(
        BOT_ADDRESS,
        data={"url": f"{current_app.config['APP_ADDRESS']}/get/{quote_plus(meme)}"},
    )

    if res.status_code == 200:
        return {"message": res.text}, 200

    return {"error": "Im ded x("}, res.status_code
