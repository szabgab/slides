import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/random">Random</a>'


    rv = web.get('/random')
    assert rv.status == '302 FOUND'
    assert 'https://' in rv.headers['Location']
    print(rv.headers['Location'])
    assert rv.headers['Location'] in app.urls
