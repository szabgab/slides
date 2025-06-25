from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/", headers={"x-some-field": "a value"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    assert response.headers == {'content-length': '25', 'content-type': 'application/json'}

