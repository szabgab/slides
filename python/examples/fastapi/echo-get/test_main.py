from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'text'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }]}

def test_main_param():
    response = client.get("/?text=Foo Bar")
    assert response.status_code == 200
    assert response.json() == {'message': "You wrote: 'Foo Bar'"}
