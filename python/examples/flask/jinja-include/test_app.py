import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<title>Code Maven Jinja include example</title>' in rv.data
    assert b'<h1>Code Maven Jinja include example</h1>' in rv.data
    assert b'Timeless' in rv.data
