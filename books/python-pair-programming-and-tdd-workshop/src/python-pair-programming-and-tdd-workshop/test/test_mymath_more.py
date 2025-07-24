import mymath

def test_div():
    assert mymath.div(6, 3)  == 2
    assert mymath.div(42, 2) == 21
 
def test_add():
    assert mymath.add(2, 2)  == 4
    assert mymath.add(0, 0) == 0
    assert mymath.add(-1, 1) == 0
    assert mymath.add(19, 23) == 42

