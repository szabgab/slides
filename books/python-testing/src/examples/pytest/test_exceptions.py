import pytest

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by Zero')
    return a / b

def test_zero_division():
    with pytest.raises(ValueError) as err:
        divide(1, 0)
    assert str(err.value) == 'Cannot divide by Zero'

#divide(3, 0)
