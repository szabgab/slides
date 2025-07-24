import pytest

@pytest.fixture(autouse = True)
def configuration():
    print("Before")

