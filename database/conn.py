# coding=utf-8
import sqlite3
import os
__author__ = 'dolacmeo'

DATABASE = os.path.dirname(__file__) + "\\test.db"


def connect_db():
    print DATABASE
    return sqlite3.connect(DATABASE)

if __name__ == '__main__':
    pass
