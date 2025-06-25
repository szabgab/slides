import application

def test_add_user_foo():
    app = application.App()
    app.add_user("Foo")
    assert app.get_user() == 'Foo'

def test_add_user_bar():
    app = application.App()
    app.add_user("Bar")
    assert app.get_user() == 'Bar'

