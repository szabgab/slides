import pytest

@pytest.fixture(autouse = True)
def configuration():
    print("Before")

    yield

    print("After")

def test_app():
    print("In test")
    assert True

