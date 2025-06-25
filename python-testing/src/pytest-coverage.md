# PyTest: Test Coverage

{% embed include file="src/examples/pytest/coverage/mymod.py" %}
{% embed include file="src/examples/pytest/coverage/test_mymod.py" %}

```
pip install pytest-cov

pytest --cov=mymod --cov-report html --cov-branch

Open htmlcov/index.html
```

