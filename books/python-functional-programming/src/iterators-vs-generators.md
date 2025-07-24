# Iterators vs Generators

* a generator is an iterator
* an iterator is an iterable

{% embed include file="src/examples/generators/iterable.py" %}

* Genarators are a simpler way to create an iterable object than iterators, but iterators allow for more complex iterables.
* To create an iterator we need a class with two methods:  `__iter__` and `__next__`, and a `raise StopIteration`.
* To create a generator we only need a single function with `yield  .


