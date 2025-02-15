import uuid
from flask import Flask, request, render_template, jsonify, abort, redirect, session

app = Flask(__name__)
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
uid = uuid.uuid5(secret, "administrator")
print(uid)

#{'is_admin': True, 'uid': '02ec19dc-bb01-5942-a640-7099cda78081', 'username': 'administrator'}
