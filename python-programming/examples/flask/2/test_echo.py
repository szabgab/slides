import echo

def test_app():
    web = echo.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/echo" method="POST">' in rv.data.decode('utf-8')

    rv = web.post('/echo', data={ "text": "foo bar" })
    assert rv.status == '200 OK'
    assert "You said: foo bar" in rv.data.decode('utf-8')

