# Unbound or infinite iterator

So far each iterator had a beginning and an end. However we can also create infinte or unbounded iterators.
The nice thing about them is that we can pass them around as we do with any other object and we can execute
operations on them without burning our CPU.

Of course the user will have to be carefull not to try to flatten the iterator, not to try to get all the values
from it, as that will only create an infinite loop or a never ending operation.

In this very simple example we count from 0 and we never stop.

When we use the `Counter` in the `for` loop we need to include a stop-condition, otherwise our loop will never end.

{% embed include file="src/examples/iterators/iterator.py" %}

**Output:**

{% embed include file="src/examples/iterators/iterator.out" %}


