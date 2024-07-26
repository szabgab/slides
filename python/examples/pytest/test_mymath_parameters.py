import mymath
import pytest

def test_add_all():
    assert mymath.add(2, 3)  == 5
    assert mymath.add(-1, 1)  == 0

def test_add_1():
    assert mymath.add(2, 3)  == 5

def test_add_2():
    assert mymath.add(-1, 1)  == 0

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, result):
    assert mymath.add(a, b)  == result


def test_div():
    assert mymath.div(6, 3)  == 2
    assert mymath.div(42, 1) == 42
