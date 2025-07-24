# Generator: function with yield - call next

* next
* yield
* StopIteration

We can create a function that has multiple `yield` expressions inside.
We call the function and what we get back is a `generator`.
A `generator` is also an `iterator` so we can call the `next` function on it and it will give us the next `yield` value.

If we call it one too many times we get a `StopIteration` exception.

{% embed include file="src/examples/generators/simple_generator_next.py" %}

**Output:**

{% embed include file="src/examples/generators/simple_generator_next.out" %}


