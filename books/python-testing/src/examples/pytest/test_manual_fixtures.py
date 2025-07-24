import pytest

@pytest.fixture()
def blue():
   print("Blue setup")
   yield
   print("Blue teardown")

@pytest.fixture()
def green():
   print("Green setup")
   yield
   print("Green teardown")

#def test_try(yellow):
#    print("yellow")

def test_one(blue, green):
   print("    Test one")


def test_two(green, blue):
   print("    Test two")
   assert False
