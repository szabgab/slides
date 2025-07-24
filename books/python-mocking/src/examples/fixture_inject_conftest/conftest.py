import pytest

@pytest.fixture()
def config():
    return {
       'name'  : 'Foo Bar',
       'email' : 'foo@bar.com',
    }


