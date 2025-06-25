# Pytest quiet mode

* -q

```
$ pytest -q test_mymod_1.py
.
1 passed in 0.01 seconds
```


```
$ pytest -q test_mymod_2.py

.F
=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
1 failed, 1 passed in 0.09 seconds
```


