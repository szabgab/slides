import mymath

def test_math():
    assert mymath.add(2, 3)  == 5
    assert mymath.div(6, 3)  == 2
    assert mymath.div(42, 1) == 42
    assert mymath.add(-1, 1) == 0
