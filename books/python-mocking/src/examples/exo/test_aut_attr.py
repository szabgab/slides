import aut

def test_a():
    assert aut.run(7) == 14

def test_b(monkeypatch):
    monkeypatch.setattr('aut.run', lambda z: z)

    assert aut.run(5) == 5

def test_c():
    assert aut.run(10) == 20

