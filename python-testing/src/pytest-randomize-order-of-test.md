# PyTest: Randomize Order of tests

Install [pytest-random-order](https://pypi.python.org/pypi/pytest-random-order)

```
pip install pytest-random-order
```

And from now we can use the `--random-order` flag to run the tests in a random order.

```
pytest -v --random-order

test_order.py::test_two PASSED
test_order.py::test_three PASSED
test_order.py::test_one PASSED
```


