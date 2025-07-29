# Type in unannotated function

{% embed include file="src/examples/python-types-at-pyweb-2025-01/unannotated_function.py" %}

```
$ mypy unannotated_function.py
unannotated_function.py:3:5: note: By default the bodies of untyped functions are not checked, consider using --check-untyped-defs  [annotation-unchecked]
Success: no issues found in 1 source file


$ mypy --check-untyped-def unannotated_function.py
unannotated_function.py:3:19: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
Found 1 error in 1 file (checked 1 source file)


$ mypy --strict unannotated_function.py
unannotated_function.py:2:1: error: Function is missing a return type annotation  [no-untyped-def]
unannotated_function.py:2:1: note: Use "-> None" if function does not return a value
unannotated_function.py:3:19: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
unannotated_function.py:6:1: error: Call to untyped function "do_something" in typed context  [no-untyped-call]
Found 3 errors in 1 file (checked 1 source file)
```
---

* --check-untyped-def
* --strict
