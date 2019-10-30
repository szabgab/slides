import pytest

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by Null')
    return a / b

def test_zero_division():
    with pytest.raises(ValueError) as e:
        divide(1, 0)
    assert str(e.value) == 'Cannot divide by Zero' 

