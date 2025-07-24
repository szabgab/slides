# Iterator: a counter

* StopIteration
* next
* __iter__
* __next__

We can create a iterator using a class. We are required to implement the `__iter__` method that returns the iterator object
and the `__next__` method that returns the next element in our iteration. We can indicated that the iteration was exhaused
by raising a `StopIteration` exception.

The instance-object that is created from this class-object is the iterator, not the class-object itself!


* `__iter__`
* `__next__` (in Python 2 this used to called `next`)
* `raise StopIteration`

{% embed include file="src/examples/iterators/counter.py" %}


