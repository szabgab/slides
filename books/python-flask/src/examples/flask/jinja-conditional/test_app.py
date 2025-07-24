import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

    rv = web.post('/echo', data={ 'text': 'foo bar' })
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said: <b>foo bar</b>' in rv.data

    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said' not in rv.data
    assert b'You did not say anything.' in rv.data

