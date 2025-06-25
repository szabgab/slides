from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    #assert response.headers == {'content-length': '25', 'content-type': 'application/json'}
    assert response.headers == {'content-length': '25', 'content-type': 'application/json', 'x-something-else': 'some value'}

