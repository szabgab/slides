import app

def test_random_sum(monkeypatch):
    values = [2, 3, 4]
    monkeypatch.setattr(app.random, 'randint', lambda x, y: values.pop(0))
    result = app.random_sum(3)
    assert result == 9
