from . import blueprint
from utils import token_required, unauthenticated, with_db
from utils import User, UserEncoder
from flask import request, render_template, session, render_template_string
import json


@blueprint.route("/register", methods=["GET"])
@unauthenticated
def register_page():
    return render_template(
        "auth.html", page_title="Join our community", action="Register"
    )


@blueprint.route("/register", methods=["POST"])
@unauthenticated
@with_db
def register(db):
    data = request.form

    if not data or "username" not in data or "password" not in data:
        return {"error": "Missing data"}, 400

    username = data["username"]
    password = data["password"]

    if (
        not username.isalnum()
        or not password.isalnum()
        or len(username) < 5
        or len(password) < 32
    ):
        return {"error": "Invalid username/password"}, 400

    user = db.find_user(username)
    if user is not None:
        return {"error": "Better luck next time"}, 400

    id = db.add_user(username, password)
    db.commit()
    session["user"] = json.dumps(User(id, username, password), cls=UserEncoder)

    return {}, 302, {"Location": "/"}


@blueprint.route("/login", methods=["GET"])
@unauthenticated
def login_page():
    return render_template("auth.html", page_title="Henlo, who dis", action="Login")


@blueprint.route("/login", methods=["POST"])
@unauthenticated
@with_db
def login(db):
    data = request.form
    if not data or "username" not in data or "password" not in data:
        return {"error": "Missing data"}, 400
    username = data["username"]
    password = data["password"]

    user = db.find_user(username)
    if user is None or password != user[2]:
        return {"error": "Invalid credentials"}, 302

    session["user"] = json.dumps(User(user[0], user[1], user[2]), cls=UserEncoder)
    return {}, 302, {"Location": "/"}


@blueprint.route("/logout", methods=["GET"])
@token_required
def logout(user):
    session.pop("user", default=None)
    return {}, 302, {"Location": "/"}


@blueprint.route("/user", methods=["GET"])
@token_required
def user_info(user):
    return render_template_string(f"uid={user.id}({{{{name}}}})", name=user.name), 200


@blueprint.route("/memes", methods=["GET"])
@token_required
@with_db
def user_memes(db, user):
    return (
        render_template_string('{"memes": {{memes}}}', memes=db.user_memes(user.id)),
        200,
    )


@blueprint.route("/comments", methods=["GET"])
@token_required
@with_db
def user_comments(db, user):
    return (
        render_template_string(
            '{"comments": {{comments}}}', comments=db.user_comments(user.id)
        ),
        200,
    )
