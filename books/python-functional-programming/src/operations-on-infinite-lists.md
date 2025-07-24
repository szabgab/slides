# Operations on infinite lists

In this example we can say that the `fibonacci()` function returns the infinite list of Fibonacci numbers.
In normal circumstances only mathematicians can work with "infinite lists", programmers are constrained by memory and time.
However generators in Python are lazy so they only pretend to be infinite lists. They are only the promise of having an
infinite list. So you can do all kinds of interesting operations on them.

In this example we multiply each value by 2. (I know it is not the most sophisticated mathematical problem, but it will work for this example.)

The variable `double_fibonacci` holds the values of the Fibonacci series multiplied by 2. More precisely it holds the
possibility to iterate over that infinite list.

So in reality we don't operate on the infinite lists, only on the "potential of the lists", but the former sounds cooler.

Try running it without the `if` and `break` statements and see what happens. (Ctrl-C will stop the program.)

{% embed include file="src/examples/generators/infinite_operations.py" %}

**Output:**

{% embed include file="src/examples/generators/infinite_operations.out" %}


