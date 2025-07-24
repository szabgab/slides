# PyTest: Order of tests

Pytest runs the test in the same order as they are found in the test module:


{% embed include file="src/examples/pytest/order/test_order.py" %}

```
pytest -v

test_order.py::test_one PASSED
test_order.py::test_two PASSED
test_order.py::test_three PASSED
```


