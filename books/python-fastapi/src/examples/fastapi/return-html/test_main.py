from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b'<a href="/hello">hello</a>'

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

