# Define the return type

{% embed include file="src/examples/python-types-at-pyweb-2025-01/variable_and_function_with_return_type.py" %}

```
$ mypy variable_and_function_with_return_type.py
variable_and_function_with_return_type.py:8:15: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```


