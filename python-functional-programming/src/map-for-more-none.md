# replace None (for Python 2)

In Python 2 map used to extend the shorter lists by **None** values.
So to avoid exceptions, we had some exra code replacing the None values by 0, using the ternary operator.

{% embed include file="src/examples/functional/map_add_none.py" %}


