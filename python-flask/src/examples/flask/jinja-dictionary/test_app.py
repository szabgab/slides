import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<h1>Person</h1>' in rv.data
    assert b'<h2>Mary Ann</h2>' in rv.data
    assert b'<td>Mary</td>' in rv.data
