# Duplicate importing of functions

{% embed include file="src/examples/modules/duplicate_add_from_module.py" %}

The second declaration silently overrides the first declaration.


[pylint](http://www.pylint.org/) can find such problems, along with a bunch of others.

```
pylint --disable=C  duplicate_add_from_module.py
```

{% embed include file="src/examples/modules/duplicate_add_from_module_lint.out" %}



