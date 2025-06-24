# List comprehension vs Generator Expression - lazy evaluation

The second big difference between list comprehension and generator expressions is that the latter has lazy evaluation.
In this example you can see that once we assign to list comprehension to a variable the `sqr` function is called on each element.

In the case of the generator expression, only when we iterate over the elements will Python call the `sqr` function.
If we exit from the loop before we go over all the values than we saved time by not executing the expression on every
element up-front. If the computation is complex and if our list is long, this can have a substantial impact.

{% embed include file="src/examples/generators/list_comprehension_generator.py" %}

**Output:**

{% embed include file="src/examples/generators/list_comprehension_generator.out" %}



