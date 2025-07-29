from anagram import is_anagram

def test_anagram():
    assert is_anagram("silent", "listen")
    assert is_anagram("bad credit", "debit card")

def test_not_anagram():
    assert not is_anagram("abc", "def")

def test_should_be_anagram_spaces():
    assert is_anagram("anagram", "nag a ram")


def test_should_be_anagram_case():
    assert is_anagram("Silent", "Listen")
