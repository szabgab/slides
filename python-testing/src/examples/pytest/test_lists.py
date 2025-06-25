import string
import re

def get_list(s):
    return list(string.printable + s + string.printable)

def test_long_lists():
    assert get_list('a') == get_list('b')
