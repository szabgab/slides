import pytest

@pytest.fixture(autouse = True, scope="module")
def fix_module():
   print("\nFix module setup")
   yield
   print("\nFix module teardown")


@pytest.fixture(autouse = True, scope="function")
def fix_function():
   print("\nFix function setup")
   yield
   print("\nFix function teardown")


@pytest.fixture()
def blue():
   print("\nFix blue setup")
   yield
   print("\nFix blue teardown")

@pytest.fixture()
def green():
   print("\nFix green setup")
   yield
   print("\nFix green teardown")


def test_one(blue, green):
   print("Test one")


def test_two(green, blue):
   print("Test two")
