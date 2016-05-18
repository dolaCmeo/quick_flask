# coding=utf-8
from flask import Flask
from flask_site.homepage import index_page
__author__ = 'dolacmeo'

app = Flask(__name__)
app.config['DEBUG'] = True
app.register_blueprint(index_page)


if __name__ == '__main__':
    app.run('0.0.0.0')
    pass
