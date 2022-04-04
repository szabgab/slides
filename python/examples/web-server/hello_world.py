from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

import time

def hello_world(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    res = f"Hello World {time.time()}".encode('utf-8')
    return [res]

port = 8080
with make_server('0.0.0.0', port, hello_world) as httpd:
    print("Serving on port {}...".format(port))
    httpd.serve_forever()

