from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_main_param():
    response = client.post("/", json={"text": "Foo Bar"})
    assert response.status_code == 200
    assert response.json() == {'message': "You wrote: 'Foo Bar'"}
