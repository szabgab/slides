from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

import time
import cgi

def hello_world(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)

    form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
    html = ''
    for f in form:
       html += f + '==' + form[f].value + '<br>'

    if not html:
        html = """
<a href="?fname=Foo&lname=Bar">click</a>
<form>
Username: <input name="username" /><br>
Password: <input type="password" name="pw" /><br>
Age group: Under 18 <input type="radio" name="age" value="kid" >
18-30 <input type="radio" name="age" value="young" >
30- <input type="radio" name="age" value="old" >
<input type="submit" value="Send" />
</form>
"""
    return html

httpd = make_server('', 8000, hello_world)
print("Serving on port 8000...")
httpd.serve_forever()
