# Define the type of variables

{% embed include file="src/examples/python-types-at-pyweb-2025-01/variable_and_function.py" %}

```
$ mypy variable_and_function.py
variable_and_function.py:7:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)


$ mypy --strict variable_and_function.py
variable_and_function.py:2:1: error: Function is missing a return type annotation  [no-untyped-def]
Found 1 error in 1 file (checked 1 source file)
```


