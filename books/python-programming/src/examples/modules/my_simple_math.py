def div(a, b):
    '''
    >>> div(8, 2)
    4
    '''
    return a/b

def add(a, b):
    '''
    >>> add(2, 2)
    4
    '''
    return a * b   # bug added on purpose!

def test_div():
    assert div(6, 3) == 2
    assert div(0, 10) == 0
    assert div(-2, 2) == -1
    #assert div(10, 0) == ??

def test_add():
    assert add(2, 2) == 4
    #assert add(1, 1) == 2


if __name__ == "__main__":
    test_div()
    test_add()
