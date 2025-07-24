# for loop with transformation


There are many cases when we have a list of some values and we need to apply some transformation to each value. At the end we would
like to have the list of the resulting values.

A very simple such transformation would be to double each value. Other, more interesting examples might be reversing each string,
computing some more complex function on each number, etc.)

In this example we just double the values and use **append** to add each value to the list containing the results.

{% embed include file="src/examples/functional/double.py" %}

**Output:**

{% embed include file="src/examples/functional/double.out" %}

There are better ways to do this.

