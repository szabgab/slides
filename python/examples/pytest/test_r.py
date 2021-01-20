import pytest

def test_pass():
    assert True

def test_fail():
    assert False

@pytest.mark.skip(reason="Unconditional skip")
def test_with_skip():
    assert True

@pytest.mark.skipif(True, reason="Conditional skip")
def test_with_skipif():
    assert True

@pytest.mark.xfail(reason = "Expect to fail and failed")
def test_with_xfail_and_fail():
   assert False

@pytest.mark.xfail(reason = "Expect to fail but passed")
def test_with_xfail_but_pass():
   assert True
