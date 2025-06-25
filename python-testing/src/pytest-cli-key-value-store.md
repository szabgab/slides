# Pytest CLI key-value store

* This is a similar application - a file-base key-value store - where the data files is computed from the name of the program: `store.json`.
* Runing two tests in parallel will make the tests collide by using the same data file.

{% embed include file="src/examples/pytest/key-value-store/store.py" %}
{% embed include file="src/examples/pytest/key-value-store/test_store.py" %}


