import math

def test_gcd():
    assert math.gcd(6, 9) == 3
    assert math.gcd(17, 9) == 1

def test_ceil():
    assert math.ceil(0) == 0
    assert math.ceil(0.1) == 1
    assert math.ceil(-0.1) == 0

def test_factorial():
    assert math.factorial(0) == 1
    assert math.factorial(1) == 1
    assert math.factorial(2) == 2
    assert math.factorial(3) == 6

