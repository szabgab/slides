import pytest

@pytest.fixture()
def config():
    return {
       'name'  : 'Foo Bar',
       'email' : 'foo@bar.com',
    }

def test_some_data(config):
    assert True
    print(config)
