import pytest
import application


@pytest.fixture()
def myapp():
    print('myapp starts')
    app = application.App()

    yield app

    app.shutdown()
    print('myapp ends')

def test_add_user_foo(myapp):
    myapp.add_user("Foo")
    assert myapp.get_user() == 'Foo'

def test_add_user_bar(myapp):
    myapp.add_user("Bar")
    assert myapp.get_user() == 'Bar'

