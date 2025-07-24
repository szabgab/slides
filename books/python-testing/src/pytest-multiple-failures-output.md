# PyTest: Multiple Failures output

```
test_failures.py .F.F.
```

```
$ pytest -v test_failures.py

test_failures.py::test_one PASSED
test_failures.py::test_two FAILED
test_failures.py::test_three PASSED
test_failures.py::test_four FAILED
test_failures.py::test_five PASSED
```

```
$ pytest -s test_failures.py

one
three
five
```


