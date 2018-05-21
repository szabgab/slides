import aud

def test_a():
    assert aud.data == {
        'name' : 'foo',
        'age'  : 42
    }

def test_b(monkeypatch):
    monkeypatch.setitem(aud.data, 'name', 'bar')

    assert aud.data == {
        'name' : 'bar',
        'age'  : 42
    }

def test_c():
    assert aud.data == {
        'name' : 'foo',
        'age'  : 42
    }

