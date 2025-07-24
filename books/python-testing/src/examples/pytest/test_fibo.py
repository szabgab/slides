import fibo

def test_fibonacci_number():
    assert fibo.fibonacci_number(1) == 1
    assert fibo.fibonacci_number(2) == 1
    assert fibo.fibonacci_number(3) == 2
    assert fibo.fibonacci_number(4) == 2

def test_fibo():
    assert fibo.fibonacci_list(1) == [1]
    assert fibo.fibonacci_list(2) == [1, 1]
    assert fibo.fibonacci_list(3) == [1, 1, 2]
