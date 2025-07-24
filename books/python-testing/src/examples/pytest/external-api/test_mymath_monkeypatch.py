import mymath

def mocked_remote_compute(x):
    print(f"mocked received {x}")
    if x == 3:
        return 9
    if x == 4:
        return 16


def test_compute(monkeypatch):
    monkeypatch.setattr(mymath.externalapi, 'remote_compute', mocked_remote_compute)
    assert mymath.compute(3, 4) == 5
    ...

def test_other(monkeypatch):
    def mocked_remote_compute(x):
        print(f"other mocked received {x}")
        if x == 6:
            return 36
        if x == 8:
            return 64
    monkeypatch.setattr(mymath.externalapi, 'remote_compute', mocked_remote_compute)
    assert mymath.compute(6, 8) == 10
    ...
