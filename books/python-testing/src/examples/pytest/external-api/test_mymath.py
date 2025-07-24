import mymath

def mocked_remote_compute(x):
    print(f"mocked received {x}")
    if x == 3:
        return 9
    if x == 4:
        return 16

mymath.externalapi.remote_compute = mocked_remote_compute

def test_compute():
    assert mymath.compute(3, 4) == 5


def test_other():
    res = mymath.compute(2, 7)
    ...
