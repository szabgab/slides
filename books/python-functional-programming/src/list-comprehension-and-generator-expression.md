# List comprehension and Generator Expression

However, before learning about `yield` let's see an even simpler way to create a generator. What we call a generator expression.

You are probably already familiar with "list comprehensions" where you have a `for` expression inside square brackets. That returns a `list` of values.

If you replace the square brackets with parentheses then you get a **generator expression**.

You can iterate over either of those. So what's the difference?


The generator expression delays the execution of the loop and the expression inside to the point where you actually need the value and it is only an object, not the full list.

So you also save memory.

{% embed include file="src/examples/generators/list_vs_generator.py" %}

**Output:**

{% embed include file="src/examples/generators/list_vs_generator.out" %}



