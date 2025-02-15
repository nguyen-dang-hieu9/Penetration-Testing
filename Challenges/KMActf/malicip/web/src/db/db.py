import mysql.connector

from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DB_SERVER'],
            port = current_app.config['DB_PORT'],
            user = current_app.config['DB_USER'],
            password = current_app.config['DB_PASSWORD'],
            database  = current_app.config['DB_DBNAME']
        )

    return g.db

def query_db(sql):
    cursor = get_db().cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db(app):
    app.teardown_appcontext(close_db)


