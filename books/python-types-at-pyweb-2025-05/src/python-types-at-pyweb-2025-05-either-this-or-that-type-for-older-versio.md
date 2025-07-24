# Either this or that type for Python before 3.10

* Union

{% embed include file="src/examples/python-types-at-pyweb-2025-05/union.py" %}
```
$ python union.py
int
str
float

$ mypy union.py
union.py:8:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```


