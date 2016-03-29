# coding: utf-8
from flask import Flask
# import pages
from flask_site.homepage import index_page

app = Flask(__name__)
app.config['DEBUG'] = True
# register pages route
app.register_blueprint(index_page)


if __name__ == '__main__':
    app.run()
