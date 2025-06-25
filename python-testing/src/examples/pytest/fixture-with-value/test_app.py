import pytest
import application


@pytest.fixture()
def app():
    print('app starts')
    myapp = application.App()
    return myapp


def test_add_user_foo(app):
    app.add_user("Foo")
    assert app.get_user() == 'Foo'

def test_add_user_bar(app):
    app.add_user("Bar")
    assert app.get_user() == 'Bar'

