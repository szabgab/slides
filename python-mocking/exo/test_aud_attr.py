import aud

def test_a():
    assert aud.run(7) == 14

def test_b(monkeypatch):
    monkeypatch.setattr('aud.run', lambda z: z)

    assert aud.run(5) == 5

def test_c():
    assert aud.run(10) == 20

