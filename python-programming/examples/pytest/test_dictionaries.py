import string
import re

def get_dictionary(k, v):
    d = dict([x, ord(x)] for x in  string.printable)
    d[k] = v
    return d

def test_big_dictionary_different_value():
    assert get_dictionary('a', 'def') == get_dictionary('a', 'abc')

def test_big_dictionary_differnt_keys():
    assert get_dictionary('abc', 1) == get_dictionary('def', 2)

