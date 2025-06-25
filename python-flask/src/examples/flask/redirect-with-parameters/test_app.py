import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/goto" method="POST">' in rv.data

    rv = web.post('/goto', data={'username': 'Joe'})
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == 'http://localhost/user/Joe'
    assert b'<p>You should be redirected automatically to target URL: <a href="/user/Joe">/user/Joe</a>' in rv.data

    rv = web.post('/goto')
    assert rv.status == '302 FOUND'
    assert rv.headers['Location'] == 'http://localhost/user/'
    assert b'<p>You should be redirected automatically to target URL: <a href="/user/">/user/</a>' in rv.data

    rv = web.get('/user/Jane')
    assert rv.status == '200 OK'
    assert rv.data == b'Page of Jane'

    rv = web.get('/user/')
    assert rv.status == '200 OK'
    assert rv.data == b'List of users'
