import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<h1>Code Maven Jinja example</h1>' in rv.data
    assert b'<li>Hungarian</li>' in rv.data
