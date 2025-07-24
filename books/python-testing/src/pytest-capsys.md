# Pytest capture STDOUT and STDERR with capsys

* capsys

Captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.

{% embed include file="src/examples/pytest/test_greet.py" %}

```
pytest test_greet.py
```


