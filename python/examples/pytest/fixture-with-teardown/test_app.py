import pytest
import application


@pytest.fixture()
def getapp():
    print('getapp starts')
    app = application.App()

    yield app

    app.shutdown()
    print('getapp ends')

def test_add_user_foo(getapp):
    getapp.add_user("Foo")
    assert getapp.get_user() == 'Foo'

def test_add_user_bar(getapp):
    getapp.add_user("Bar")
    assert getapp.get_user() == 'Bar'

