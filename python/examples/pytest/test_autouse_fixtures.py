import pytest
import time

@pytest.fixture(autouse = True, scope="module")
def fix_module():
    answer = 42
    print(f"Module setup {answer}")
    yield
    print(f"Module teardown {answer}")


@pytest.fixture(autouse = True, scope="function")
def fix_function():
    start = time.time()
    print(f"  Function setup {start}")
    yield
    print(f"  Function teardown {start}")


def test_one():
    print("    Test one")
    assert True
    print("    Test one - 2nd part")

def test_two():
    print("    Test two")
    assert False
    print("    Test two - 2nd part")
