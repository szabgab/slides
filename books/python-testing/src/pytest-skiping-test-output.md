# Pytest: skipping tests output in verbose mode

```
$ pytest -v test_on_condition.py

test_on_condition.py::test_mac PASSED
test_on_condition.py::test_any SKIPPED
test_on_condition.py::test_windows SKIPPED
test_on_condition.py::test_linux SKIPPED

==== 1 passed, 3 skipped in 0.01 seconds ======
```


