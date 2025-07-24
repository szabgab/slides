# Travis-CI and Python with Pytest

* Simply adding `script: pytest` will not work.
* pytest will fail with exit code 5 if it cannot find any test to run.

{% embed include file="src/examples/python-pytest/.travis.yml" %}
{% embed include file="src/examples/python-pytest/test_python.py" %}


