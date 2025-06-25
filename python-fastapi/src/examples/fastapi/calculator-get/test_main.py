from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main():
    response = client.get("/?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {'message': 5}

    response = client.get("/?a=2&b=x")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['query', 'b'],
                'msg': 'value is not a valid integer',
                'type': 'type_error.integer'
            }]}
