import app

def test_app():
    app.data_file = 'test_1.json'    # manually overwrite

    res = app.do_something()       # it is now test_1.json
    ...

def test_again():
    res = app.do_something()      # it is still test_1.json
    ...
