import pytest
pytestmark = pytest.mark.random_order(disabled=True)

def test_one():
    assert True

def test_two():
    assert True

def test_three():
    assert True


