# coding: utf-8
import sqlite3
import os
from flask import Flask, g
from contextlib import closing

DATABASE = os.path.dirname(__file__) + "\\test.db"

app = Flask(__name__)


def connect_db():
    print DATABASE
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
