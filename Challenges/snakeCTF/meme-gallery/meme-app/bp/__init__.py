from flask import Blueprint

blueprint = Blueprint("app", __name__)

from . import auth
from . import meme
