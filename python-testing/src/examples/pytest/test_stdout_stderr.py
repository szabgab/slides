import sys

def test_hello():
    print("hello testing")
    print("stderr during testing", file=sys.stderr)
    assert True
