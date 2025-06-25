# Add extra command line parameters to Pytest - as a fixture

* conftest

* We can also create a fixture that will read the parameter

{% embed include file="src/examples/pytest/py2/conftest.py" %}
{% embed include file="src/examples/pytest/py2/test_one.py" %}

```
pytest -s
test_one.py None
```

```
pytest -s --demo Hello
test_one.py Hello
```


