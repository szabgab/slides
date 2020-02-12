import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/echo" method="POST">' in rv.data.decode('utf-8')


    rv = web.get('/echo')
    assert rv.status == '405 METHOD NOT ALLOWED'
    assert '<title>405 Method Not Allowed</title>' in rv.data.decode('utf-8')

    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b"Nothing to say?" == rv.data


    rv = web.post('/echo', data={ "text": "foo bar" })
    assert rv.status == '200 OK'
    assert b"You said: foo bar" == rv.data
