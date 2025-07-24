import app

def test_sum():
    app.Thing.data_file = lambda self: 'data.json'
    t = app.Thing()
    res = t.get_sum()
    assert True
    assert res == 42

