# coding: utf-8
from flask import Blueprint, render_template, request

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def index():

    return render_template('test_index.html')


@index_page.route('/bootstrap/')
def bootstrap():

    return render_template('home/bootstrap_test.html')
