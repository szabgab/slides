# Two variables of the same and different types

{% embed include file="src/examples/python-types-at-pyweb-2025-05/generics_two_types.py" %}

```
$ mypy generics_two_types.py
generics_two_types.py:10:1: error: Value of type variable "T" of "the_same" cannot be "object"  [type-var]
Found 1 error in 1 file (checked 1 source file)
```


