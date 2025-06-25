# PyTest: Run tests in parallel with xdist

* xdist

```
$ pip install pytest-xdist
$ pytest -n NUM
```

{% embed include file="src/examples/pytest/xdist/test_animals.py" %}
{% embed include file="src/examples/pytest/xdist/test_colors.py" %}

```
pytest          8.04 sec
pytest -n 2     4.64 sec
pytest -n 4     3.07 sec
```


