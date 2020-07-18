import string

def get_string():
    return string.printable * 30

def test_long_strings():
    assert 'hello' in get_string()

