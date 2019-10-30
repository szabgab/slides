from mymod_1 import is_anagram

def test_anagram():
    assert is_anagram("elvis", "lives")
    assert is_anagram("silent", "listen")
    assert not is_anagram("one", "two")

def test_multiword_anagram():
    assert is_anagram("ana gram", "naga ram")
    assert is_anagram("anagram", "nag a ram")

