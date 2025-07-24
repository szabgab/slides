import app


def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="https://code-maven.com/">Code Maven</a>' in rv.data, 'footer'
    assert b'<title>Main page</title>' in rv.data, 'title'
    assert b'This is the content' in rv.data, 'content'

