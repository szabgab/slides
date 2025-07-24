# Pytest: show skipped tests with -rs

* -rs

```
$ pytest -rs test_on_condition.py
```

```
collected 4 items

test_on_condition.py s.ss

===== short test summary info =====
SKIP [1] test_on_condition.py:15: To show we can skip tests without any condition.
SKIP [1] test_on_condition.py:7: Linux tests
SKIP [1] test_on_condition.py:11: Windows tests

==== 1 passed, 3 skipped in 0.03 seconds ====
```


