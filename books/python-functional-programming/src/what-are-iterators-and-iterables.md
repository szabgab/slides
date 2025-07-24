# What are iterators and iterables?

* All of them are iterables
* A filehandle and the map object are also iterators. (Side note: You should always `open` files using the `with` statement and not like this.)
* `iter()` would return the iterator from an iterable. We don't need this.

{% embed include file="src/examples/iterators/what_are_iterators.py" %}

**Output:**

{% embed include file="src/examples/iterators/what_are_iterators.out" %}


