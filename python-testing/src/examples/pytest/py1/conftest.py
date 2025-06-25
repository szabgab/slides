def pytest_addoption(parser):
    parser.addoption("--demo")
    parser.addoption("--noisy", action='store_true')
