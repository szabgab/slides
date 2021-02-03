import pytest

@pytest.fixture(autouse = True, scope="module")
def fix_module():
    print("\nFix module setup")
    yield
    print("\nFix module teardown")


@pytest.fixture(autouse = True, scope="function")
def fix_function():
    print("\n  Fix function setup")
    yield
    print("\n  Fix function teardown")
