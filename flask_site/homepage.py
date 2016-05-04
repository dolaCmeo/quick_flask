# coding: utf-8
from flask import Blueprint, render_template, request

index_page = Blueprint('index_page', __name__, template_folder='templates')


@index_page.route('/')
def index():

    return render_template('test_index.html')


@index_page.route('/bootstrap/')
def bootstrap():

    return render_template('home/bootstrap_test.html')

@index_page.route('/test/')
def testpage():
    testhtml = """

<!DOCTYPE html>
<html lang="zh-CN">
  <head></head>
  <body>
  <h1>Hello World</h1>
  </body>
</html>
    """
    return testhtml


@index_page.route('/dataoutput/')
def make_data(ouput_type='html'):
    from database import conn
    db = conn.connect_db()
    cursor = db.execute("SELECT id, name, address, salary  from COMPANY")
    output_html = "<ul>\r\n"
    output_list = []
    for n in cursor:
        a = "<li>"+str(n[0])+"<a title='"+n[2]+"'>"+n[1]+"</a>"+str(n[3])+"</li>\r\n"
        output_html += a
        output_list.append(a)
    output_html += "</ul>"
    if ouput_type == 'html':
        return output_html
    elif ouput_type == 'list':
        return output_list
    else:
        return 'error type!'


@index_page.route('/test2')
def other_page():
    other_data = make_data()
    testhtml = """
    <!DOCTYPE html>
    <html lang="zh-CN">
      <head></head>
      <body>
      <h1>Hello World</h1>
      %s
      </body>
    </html>
    """ % other_data
    print testhtml
    return testhtml


@index_page.route('/test3')
def oother_page():
    inputdata = make_data('html')
    list_data = make_data('list')
    return render_template('test_index.html',
                           input_data=inputdata,
                           list_data=list_data)
