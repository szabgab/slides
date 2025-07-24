import os
import pathlib
import time
import pytest


@pytest.fixture(autouse = True, scope="function", params=["name"])
def generate(name):
    print(f"Fixture before test using {name}")
    yield
    print(f"Fixture after test using {name}")

@pytest.mark.parametrize("name", ["apple"])
def test_with_param(name):
    print(f"Test using {name}")

@pytest.mark.parametrize("name", ["banana"])
def test_without_param():
    print(f"Test not using param")

