import app

def test_sum(monkeypatch):
    monkeypatch.setattr(app, 'data_file', 'test_1.json')

    res = app.do_something()    # It is now test_1.json
    ...


def test_again():
    res = app.do_something() # back to the original value
    ...
