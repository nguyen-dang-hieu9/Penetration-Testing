from functools import wraps
from flask import session, current_app
from minio import Minio
import json
import sqlite3
from os import environ, listdir
from io import BytesIO

OS_ADDRESS = environ["MINIO_ADDRESS"]
BOT_ADDRESS = environ["BOT_ADDRESS"]
DB_FILE = "file:///tmp/app.db"


class User(object):

    def __init__(self, id, username, password):
        self._id = id
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def admin(self):
        return (
            self._username == current_app.config["ADMIN_USERNAME"]
            and self._password == current_app.config["ADMIN_PASSWORD"]
        )


class UserEncoder(json.JSONEncoder):
    def default(self, user):
        return {"id": user.id, "username": user.name, "password": user.password}


class UserDecoder(json.JSONDecoder):
    def decode(self, encoded):
        parsed = json.loads(encoded)
        id = parsed["id"]
        username = parsed["username"]
        password = parsed["password"]
        if len(encoded) > 85 or len(username) < 5 or len(password) < 32:
            raise json.JSONDecodeError("Unusual behavior detected", "", 0)
        return User(id, username, password)


class AppDataStorage(object):
    def __init__(self, file, ADDRESS):
        self.conn = sqlite3.connect(file)
        self.cur = self.conn.cursor()
        self.client = Minio(f"{ADDRESS}:9000", secure=False)

    def init_schema(self):
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT NOT NULL
            );"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS memes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE NOT NULL,
            creator_id INTEGER NOT NULL,
            bucket TEXT NOT NULL,
            FOREIGN KEY(creator_id) REFERENCES users(id) ON DELETE CASCADE
            )"""
        )
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS comments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meme_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            FOREIGN KEY(meme_id) REFERENCES memes(id)  ON DELETE CASCADE,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            )"""
        )
        admin_id = self.add_user(environ["ADMIN_USERNAME"], environ["ADMIN_PASSWORD"])
        user_id = self.add_user(environ["MY_USER"], environ["MY_PASS"])
        memes = listdir("memes")
        for i, meme in enumerate(memes):
            bucket = "memes" if i < 5 else "supermemes"
            id = user_id if i < 5 else admin_id
            with open(f"memes/{meme}", "rb") as f:
                content = f.read()
                self.add_meme(meme, content, "image/jpeg", id, bucket)
        self.commit()

    def add_user(self, username, password):
        self.cur.execute(
            """INSERT OR IGNORE
            INTO users(username, password) VALUES (?, ?);""",
            (
                username,
                password,
            ),
        )
        return self.cur.lastrowid

    def add_meme(self, meme, content, content_type, creator_id, bucket):
        self.cur.execute(
            """INSERT OR IGNORE
                    INTO memes(filename, creator_id, bucket) VALUES (?, ?, ?);""",
            (
                meme,
                creator_id,
                bucket,
            ),
        )
        self.client.put_object(
            bucket, meme, BytesIO(content), len(content), content_type
        )
        return self.cur.lastrowid

    def add_comment(self, comment, user_id, meme_id):
        self.cur.execute(
            "INSERT INTO comments(content, user_id, meme_id) VALUES (?, ?, ?)",
            (
                comment,
                user_id,
                meme_id,
            ),
        )
        return self.cur.lastrowid

    def find_user(self, username):
        res = self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = res.fetchone()
        return user

    def find_meme(self, meme, bucket):
        res = self.cur.execute(
            "SELECT * FROM memes WHERE filename = ? AND bucket = ?",
            (
                meme,
                bucket,
            ),
        )
        return res.fetchone()

    def retrieve_meme_data(self, meme, bucket):
        return self.client.get_object(bucket, meme)

    def find_comments(self, meme, bucket):
        res = self.cur.execute(
            """SELECT username, content
            FROM (comments c INNER JOIN users u ON c.user_id=u.id)
                INNER JOIN memes m ON c.meme_id = m.id
            WHERE m.filename = ? and m.bucket = ?""",
            (
                meme,
                bucket,
            ),
        )
        return res.fetchall()

    def bucket_memes(self, bucket):
        res = self.cur.execute(
            "SELECT filename FROM memes WHERE bucket = ?",
            (bucket,),
        )
        return list(map(lambda x: x[0], res.fetchall()))

    def user_memes(self, id):
        res = self.cur.execute("SELECT filename FROM memes WHERE creator_id = ?", (id,))
        return list(map(lambda x: x[0], res.fetchall()))

    def user_comments(self, id):
        res = self.cur.execute(
            """SELECT filename, content 
                    FROM comments c INNER JOIN memes m ON c.meme_id = m.id
                    WHERE c.user_id = ?""",
            (id,),
        )
        rs = res.fetchall()
        comments = {}
        for image, comment in rs:
            comments.setdefault(image, []).append(comment)

        return comments

    def delete_meme(self, meme, bucket):
        self.cur.execute("DELETE FROM memes WHERE filename = ?", (meme,))
        self.client.remove_object(bucket, meme)

    def meme_bucket(self, meme):
        res = self.cur.execute(
            "SELECT bucket FROM memes WHERE filename = ?",
            (meme,),
        )
        res = res.fetchone()
        if res is None:
            return None
        return res[0]

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if not session.get("user"):
                return {"error": "Unauthorized"}, 302, {"Location": "/login"}
            logged_user = json.loads(session.get("user"), cls=UserDecoder)
            db = AppDataStorage(DB_FILE, OS_ADDRESS)
            res = db.find_user(logged_user.name)
            if res is None or res[2] != logged_user.password:
                return (
                    {"error": "Invalid token"},
                    500,
                    {"Set-Cookie": "session=;Max-Age=0;"},
                )
        except json.JSONDecodeError as e:
            session.pop("user", default=None)
            return {"error": str(e)}, 500, {"Set-Cookie": "session=;Max-Age=0;"}

        return f(logged_user, *args, **kwargs)

    return decorated


def unauthenticated(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if not (session.get("user") is None):
                logged_user = json.loads(session.get("user"), cls=UserDecoder)
                db = AppDataStorage(DB_FILE, OS_ADDRESS)
                res = db.find_user(logged_user.name)
                if res is None:
                    return (
                        {"error": "Invalid token"},
                        500,
                        {"Set-Cookie": "session=;Max-Age=0;"},
                    )

                return (
                    {"error": "Already authenticated"},
                    302,
                    {"Location": "/"},
                )
        except json.JSONDecodeError as e:
            raise e
        return f(*args, **kwargs)

    return decorated


def with_db(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        db = AppDataStorage(DB_FILE, OS_ADDRESS)
        try:
            return f(db, *args, **kwargs)
        except sqlite3.DatabaseError as e:
            return {"error": str(e)}, 500
        finally:
            db.close()

    return decorated


def bucket_for(user):
    if user.admin:
        return "supermemes"
    else:
        return "memes"
