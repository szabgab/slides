# double with lambda

There are many other cases besides **map** where we need to pass a function as a parameter to some other function.
Many cases the function we pass is some almost trivial function with a single operation in it.
In those cases creating a named function like the "double" function in the previous examples is an overkill.

In this example we also used the **list** function to force the full evaluation of the map object to make it easier to show
the results. Normally you probably would not use the **list** function here.

{% embed include file="src/examples/functional/double_lambda.py" %}

**Output:**

{% embed include file="src/examples/functional/double_lambda.out" %}


