import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/echo" method="GET">' in rv.data.decode('utf-8')

    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert b"Nothing to say?" == rv.data

    rv = web.get('/echo?text=foo+bar')
    assert rv.status == '200 OK'
    assert b"You said: foo bar" == rv.data
