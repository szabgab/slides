import string
import re

def get_lista():
    return 'a', 'b', 'c'
def get_listx():
    return 'x', 'b', 'y'

def test_short_lists():
    assert get_lista() == get_listx()
