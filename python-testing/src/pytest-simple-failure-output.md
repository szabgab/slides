# Pytest simple tests - failure output


```
$ pytest test_mymod_2.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 2 items

test_mymod_2.py .F

=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
============== 1 failed, 1 passed in 0.09 seconds ==============
```



