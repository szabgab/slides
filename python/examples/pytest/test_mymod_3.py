from mymod_1 import is_anagram
import pytest

def test_anagram():
   assert is_anagram("abc", "acb")
   assert is_anagram("silent", "listen")
   assert not is_anagram("one", "two")

@pytest.mark.xfail(reason = "Bug #42")
def test_multiword_anagram():
   assert is_anagram("ana gram", "naga ram")
   assert is_anagram("anagram", "nag a ram")

