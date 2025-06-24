# Mixing for and next

You can even use `next` inside a `for` loop, but then you will have to handle the `StopIteration` exception
that migh happen during your call of `next`.

I am not really sure when would we want to use this.

{% embed include file="src/examples/iterators/mix_for_and_next.py" %}

**Output:**

{% embed include file="src/examples/iterators/mix_for_and_next.out" %}


