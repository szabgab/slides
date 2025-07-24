# Add extra command line parameters to Pytest - conftest - getoption

* conftest

* In this case the option expects a value
* And we need to use getoption to get the value
* See [Parser](https://docs.pytest.org/en/stable/reference.html#parser)
* See [argparse](https://docs.python.org/library/argparse.html)

{% embed include file="src/examples/pytest/py1/conftest.py" %}
{% embed include file="src/examples/pytest/py1/test_one.py" %}

```
pytest -s
None
False
```

```
pytest -s --demo Hello --noisy
Hello
True
```


