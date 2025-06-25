#import pytest
#
def pytest_addoption(parser):
    parser.addoption("--demo")
#
#@pytest.fixture
#def demo(request):
#    return request.config.getoption("--demo")
