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
    if 'txt' in form:
       return 'Echo: ' + form['txt'].value

    return """
<form>
<input name="txt" />
<input type="submit" value="Echo" />
</form>
"""
httpd = make_server('', 8000, hello_world)
print("Serving on port 8000...")
httpd.serve_forever()
