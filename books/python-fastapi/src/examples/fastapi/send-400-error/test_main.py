from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_good():
    response = client.get("/user/23")
    assert response.status_code == 200
    assert response.json() == {'user': 23}

def test_bad():
    response = client.get("/user/42")
    assert response.status_code == 400
    assert response.json() == {'detail': 'User does not exist'}

