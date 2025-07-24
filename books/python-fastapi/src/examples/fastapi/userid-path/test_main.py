from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_int():
    response = client.get("/user/23")
    assert response.status_code == 200
    assert response.json() == {'user': 23}

def test_str():
    response = client.get("/user/foo")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'user_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }]}

def test_float():
    response = client.get("/user/2.3")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['path', 'user_id'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }]}

def test_nothing():
    response = client.get("/user/")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
