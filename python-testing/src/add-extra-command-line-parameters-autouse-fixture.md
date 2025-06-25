# Add extra command line parameters to Pytest - used in the autouse fixtures

* conftest


{% embed include file="src/examples/pytest/py4/conftest.py" %}
{% embed include file="src/examples/pytest/py4/test_one.py" %}

```
pytest -s --demo Hello

Module Hello
Func Hello
Func Hello
```


