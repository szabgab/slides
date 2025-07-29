# Either this or that type (Union)

* Union

* Python 3.10+

{% embed include file="src/examples/python-types-at-pyweb-2025-01/pipe.py" %}

```
$ python union.py
int
str
float

$ mypy pipe.py
pipe.py:6:9: error: Argument 1 to "my_exit" has incompatible type "float"; expected "str | int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```


