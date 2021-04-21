import mymod

def test_add():
    assert mymod.add(2, 3) == 5

def test_area():
    assert mymod.area(2, 3) == 6
    assert mymod.area(-2, 3) == None

def test_fib():
    assert mymod.fib(1) == 1
