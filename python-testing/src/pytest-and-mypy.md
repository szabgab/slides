# Pytest and mypy

```
pip install mypy
pip install pytest-mypy

mypy mymod.py

pytest --mypy
```

{% embed include file="src/examples/pytest/mypy/mymod.py" %}
{% embed include file="src/examples/pytest/mypy/test_mymod.py" %}

Excluding files when using `mypy` works, but that does not exclude them when using `pytest --mypy`

{% embed include file="src/examples/pytest/mypy/mypy.ini)

Not even this:

{% embed include file="src/examples/pytest/mypy/pytest.ini)

