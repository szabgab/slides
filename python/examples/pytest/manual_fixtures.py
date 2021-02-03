import pytest

@pytest.fixture()
def blue():
   print("Fix blue setup")
   yield
   print("Fix blue teardown")

@pytest.fixture()
def green():
   print("Fix green setup")
   yield
   print("Fix green teardown")


def test_one(blue, green):
   print("    Test one")


def test_two(green, blue):
   print("    Test two")
