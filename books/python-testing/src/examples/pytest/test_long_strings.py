import string

def get_string(s):
    return string.printable + s + string.printable

def test_long_strings():
    assert get_string('a') == get_string('b')

