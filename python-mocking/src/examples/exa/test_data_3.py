import app

def test_sum(monkeypatch):
    monkeypatch.setattr(app, 'data_file', 'test_1.json')

    res = app.get_sum()
    assert True
    assert res == 42


def test_again():
    print(app.data_file)             # it is now back to the original value
