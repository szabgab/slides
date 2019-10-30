import pytest
from banks import Bank, NegativeDeposite

def test_negative_deposit():
    b = Bank(10)
    with pytest.raises(Exception) as exinfo:
        b.deposit(-1)
    assert exinfo.type == NegativeDeposite
    assert str(exinfo.value) == 'Cannot deposit negative sum' 
