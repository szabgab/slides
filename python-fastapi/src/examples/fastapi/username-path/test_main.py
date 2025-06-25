from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_foobar():
    response = client.get("/user/foobar")
    assert response.status_code == 200
    assert response.json() == {'msg': "user 'foobar'"}

def test_foo_bar():
    response = client.get("/user/foo bar")
    assert response.status_code == 200
    assert response.json() == {'msg': "user 'foo bar'"}


def test_user():
    response = client.get("/user/")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
