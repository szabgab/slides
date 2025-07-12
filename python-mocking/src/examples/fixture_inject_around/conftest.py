import pytest

@pytest.fixture()
def configuration():
    print("Before")

    yield { 'name' : 'Foo Bar' }

    print("After")
