import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/goto">Go to</a>'

    rv = web.get('/goto')
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == 'http://localhost/user'
    assert b'<p>You should be redirected automatically to target URL: <a href="/user">/user</a>' in rv.data


    rv = web.get('/user')
    assert rv.status == '200 OK'
    assert rv.data == b'User page'
