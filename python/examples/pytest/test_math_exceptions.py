import math
import pytest

def test_math():
    with pytest.raises(Exception) as exinfo:
        math.factorial(-1)
    assert exinfo.type == ValueError
    assert str(exinfo.value) == 'factorial() not defined for negative values'


    with pytest.raises(Exception) as exinfo:
        math.factorial(1.2)
    assert exinfo.type == ValueError
    assert str(exinfo.value) == 'factorial() only accepts integral values'


