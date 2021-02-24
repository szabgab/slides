import sys
import pytest

@pytest.mark.skipif(sys.platform != 'linux', reason="Linux tests")
def test_linux():
    assert True

@pytest.mark.skip(reason="To show we can skip tests without any condition.")
def test_any():
    assert True

@pytest.fixture(autouse = True, scope="module")
def module_demo():
    print(f"Fixture")


