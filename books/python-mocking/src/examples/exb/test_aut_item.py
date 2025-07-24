import aut

def test_a():
    assert aut.data == {
        'name' : 'foo',
        'age'  : 42
    }

def test_b(monkeypatch):
    monkeypatch.setitem(aut.data, 'name', 'bar')

    assert aut.data == {
        'name' : 'bar',
        'age'  : 42
    }

def test_c():
    assert aut.data == {
        'name' : 'foo',
        'age'  : 42
    }

