import app
import re

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/time">time</a>'

def test_app():
    web = app.app.test_client()

    rv = web.get('/time')
    assert rv.status == '200 OK'
    assert re.search(r'\d+\.\d+$', rv.data.decode('utf-8'))
