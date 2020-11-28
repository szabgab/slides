import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/cm">Go to Code Maven</a>'


    rv = web.get('/cm')
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == 'https://code-maven.com/'
    assert b'<p>You should be redirected automatically to target URL: <a href="https://code-maven.com/">https://code-maven.com/</a>' in rv.data
