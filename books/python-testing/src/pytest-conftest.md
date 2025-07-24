# Share fixtures among test files: conftest.py

* conftest.py

{% embed include file="src/examples/pytest/autouse/conftest.py" %}
{% embed include file="src/examples/pytest/autouse/test_blue.py" %}
{% embed include file="src/examples/pytest/autouse/test_green.py" %}

```
pytest -qs
```

**Output:**

{% embed include file="src/examples/pytest/autouse/pytest.out" %}



