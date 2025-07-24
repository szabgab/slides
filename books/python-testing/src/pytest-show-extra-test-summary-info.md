# Pytest: show extra test summmary info with -r

* -r
* -ra

* (f)ailed
* (E)error
* (s)skipped
* (x)failed
* (X)passed
* (p)passed
* (P)passed with output
* (a)all except pP


```
pytest -rx  - xfail, expected to fail
pytest -rs  - skipped
pytest -ra  - all the special cases
```

{% embed include file="src/examples/pytest/test_r.py" %}

```
pytest -h
```


