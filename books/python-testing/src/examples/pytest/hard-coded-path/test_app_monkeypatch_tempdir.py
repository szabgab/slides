import app

def test_sum(monkeypatch, tmpdir):
    fake_file = tmpdir.join('test_1.json')
    monkeypatch.setattr(app, 'data_file', fake_file)

    res = app.do_something()
    ...

def test_again():
    res = app.do_something()    # back to the original value
    ...
