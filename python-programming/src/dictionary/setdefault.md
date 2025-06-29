# Setdefault


Trying to access a key in a dictionary that does not exist will result a KeyError exception.

Using the `get` method we can avoid this. The `get` method, will return the value of the key if the key exists. None if the key does not exists, or a default value if it was supplied to the `get` method.
This will not change the dictionary.

Using the `setdefault` method is similar to the `get` method but it will also create the key with the given value.



{% embed include file="src/examples/dictionary/setdefault.py" %}


