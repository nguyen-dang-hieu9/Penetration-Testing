#!/usr/bin/env python3
from flask import Flask, render_template
from os import environ
from bp import blueprint
from utils import AppDataStorage
from utils import DB_FILE, OS_ADDRESS
from random import randbytes
import sys


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024  # Max size
app.config["SECRET_KEY"] = environ.get("SECRET_KEY", None) or randbytes(4)
app.config["ADMIN_USERNAME"] = environ.get("ADMIN_USERNAME", "")
app.config["ADMIN_PASSWORD"] = environ.get("ADMIN_PASSWORD", "")
app.config["APP_ADDRESS"] = environ.get("APP_ADDRESS", "http://localhost:3000")

app.register_blueprint(blueprint)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", page_title="Meme gallery")


with app.app_context():
    db = AppDataStorage(DB_FILE, OS_ADDRESS)
    db.init_schema()
    db.close()
