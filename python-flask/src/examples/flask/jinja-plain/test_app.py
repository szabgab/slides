import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

    rv = web.post('/echo', data={'text': 'Hello'})
    assert rv.status == '200 OK'
    assert b'You said: Hello' == rv.data

    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'You said: ' == rv.data
