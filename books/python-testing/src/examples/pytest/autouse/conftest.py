import pytest

@pytest.fixture(autouse = True, scope="session")
def fix_session():
    print("\nSession setup")
    yield
    print("\nSession teardown")


@pytest.fixture(autouse = True, scope="module")
def fix_module():
    print("\n  Module setup")
    yield
    print("\n  Module teardown")


@pytest.fixture(autouse = True, scope="function")
def fix_function():
    print("\n    Function setup")
    yield
    print("\n    Function teardown")
