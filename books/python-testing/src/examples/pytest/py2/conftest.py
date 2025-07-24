import pytest

def pytest_addoption(parser):
    parser.addoption("--demo")

@pytest.fixture
def mydemo(request):
    return request.config.getoption("--demo")
