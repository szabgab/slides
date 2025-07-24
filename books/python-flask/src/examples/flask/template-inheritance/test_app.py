import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="https://code-maven.com/">Code Maven</a>' in rv.data, 'footer'
    assert b'<title>Demo: Main page</title>' in rv.data, 'main title'
    assert b'This is the content' in rv.data, 'main page content'
    assert b'original' not in rv.data, 'no inherited content'

def test_page():
    web = app.app.test_client()

    rv = web.get('/page')
    assert rv.status == '200 OK'
    assert b'<a href="https://code-maven.com/">Code Maven</a>' in rv.data, 'footer'
    assert b'<title>Demo: Other page</title>' in rv.data, 'page title'
    assert b'The original content' in rv.data, 'page content'
    assert b'This is the content' in rv.data, 'inherited content'

