# mypy generics - cannot be any type

{% embed include file="src/examples/python-types-at-pyweb-2025-01/generics_cannot_be_any_type.py" %}

```
mypy generics_cannot_be_any_type.py

generics_limit_types_by_listing.py:2:12: error: Unsupported left operand type for + ("T")  [operator]
Found 1 error in 1 file (checked 1 source file)
```


