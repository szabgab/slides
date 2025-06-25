from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_shallow_one():
    response = client.get("/shallow/a.txt")
    assert response.status_code == 200
    assert response.json() == {'shallow': 'a.txt'}

def test_shallow_more():
    response = client.get("/shallow/a/b.txt")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_deep_one():
    response = client.get("/deep/a.txt")
    assert response.status_code == 200
    assert response.json() == {'deep': 'a.txt'}

def test_deep_more():
    response = client.get("/deep/a/b.txt")
    assert response.status_code == 200
    assert response.json() == {'deep': 'a/b.txt'}

