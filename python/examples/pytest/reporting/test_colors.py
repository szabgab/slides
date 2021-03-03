import pytest

def test_blue():
    pass

def test_red():
    assert 1 == 2

@pytest.mark.skip(reason="So we can show skip reporting")
def test_purple():
    assert 1 == 3

@pytest.mark.xfail(reason = "To show xfail that really fails")
def test_orange():
    1 == 4

@pytest.mark.xfail(reason = "To show xfail that passes")
def test_green():
    pass
