import app
import pytest

@pytest.fixture()
def web():
    return app.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Main<br>' in rv.data

@pytest.mark.parametrize('uid', ['23', '42', 'Joe'])
def test_user(web, uid):
    rv = web.get(f'/user/{uid}')
    assert rv.status == '200 OK'
    assert uid == rv.data.decode('utf-8')

def test_user_fail(web):
    rv = web.get(f'/user/')
    assert rv.status == '404 NOT FOUND'

def test_user_fail(web):
    rv = web.get(f'/user')
    assert rv.status == '404 NOT FOUND'


