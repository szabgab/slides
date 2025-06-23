# reduce

In Python 2 it was still part of the language.

`reduce(function, iterable[, initializer])`

{% embed include file="src/examples/functional/reduce.py" %}
{% embed include file="src/examples/functional/reduce.out" %}

The initializer is used as the 0th element returned by the iterable. It is mostly interesting in case the iterable is empty.


