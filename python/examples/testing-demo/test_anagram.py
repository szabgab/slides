from anagram import is_anagram

def test_anagram():
    assert is_anagram("silent", "listen")
    assert is_anagram("bad credit", "debit card")

def test_not_anagram():
    assert not is_anagram("abc", "def")

def test_should_be_anagram():
    assert is_anagram("anagram", "nag a ram")
