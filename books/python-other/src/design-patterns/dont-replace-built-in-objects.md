# Don't replace built-in objects

{% embed include file="src/examples/patterns/replace_print.py" %}


```
pip install flake8-builtins
flake8 --ignore=   replace_print.py

replace_print.py:3:1: A001 "print" is a python builtin and is being shadowed, consider renaming the variable
```


