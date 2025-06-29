def test_add():
    print('Testing  {}'.format(__file__))
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    # assert add(-99, 1) == 0 # AssertionError

def add(a, b):
    return a + b

if __name__ == '__main__':
    test_add()
