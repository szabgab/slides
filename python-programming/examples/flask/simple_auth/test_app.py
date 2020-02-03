import app
import base64

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'Hello World!'

def test_admin_unauth():
    web = app.app.test_client()

    rv = web.get('/admin')
    assert rv.status == '401 UNAUTHORIZED'
    assert rv.data == b'Unauthorized Access'
    assert 'WWW-Authenticate' in rv.headers
    assert rv.headers['WWW-Authenticate'] == 'Basic realm="Authentication Required"'

def test_admin_auth():
    web = app.app.test_client()

    credentials = base64.b64encode(b'john:nhoj').decode('utf-8')
    rv = web.get(f'/admin', headers={
            'Authorization': 'Basic ' + credentials
    })

    assert rv.status == '200 OK'
    assert rv.data == b'Hello Admin'
