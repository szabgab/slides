from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_Volvo():
    response = client.get("/car/Volvo")
    assert response.status_code == 200
    assert response.json() == {'car_type': 'Volvo'}

def test_volvo():
    response = client.get("/car/volvo")
    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'ctx': {'enum_values': ['Tesla', 'Volvo', 'Fiat']},
                'loc': ['path', 'car_type'],
                'msg': 'value is not a valid enumeration member; permitted: ' "'Tesla', 'Volvo', 'Fiat'",
                'type': 'type_error.enum'
            }]}


