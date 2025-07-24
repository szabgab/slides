# map

* `map(function, iterable, ...)`

The [map](https://docs.python.org/library/functions.html#map) function of Python applies a function to every item in an iterable and returns an iterator
that can be used to iterate over the results. Wow, how many times I repeated the word iter...something. Instead of trying to untangle that sentence,
let's look at the following example:

We have a list of numbers in the brilliantly named variable `numbers` with 7, 2, 4, 1 as the content. We would like to create a list of all the doubles (so that would be 14, 4, 8, 2 in this case)
and then iterate over them printing them on the screen. Sure, you probably have some more complex operation to do on the numbers than to simply double them, but in this example I did not want to complicate
that part. Suffice to say that you have some computation to do on every element of the original list.

So you encapsulate your computation in a regular Python function (in our case the function is called **double**). Then you call **map** and pass to it two parameters. The first parameter is the **double** function itself, the second parameter is the list of the values you would like to work on. `map` will go over all the values in the **numbers** list, call the **double** function with
each number and return you somthing that will allow you to iterate over the results. Something like this:


```
double_numbers = [ double(7), double(2), double(4), double(1)]
```


Except, that the above is not true.

When Python executes the `double_numbers = map(double, numbers)` line, no computation happens and no resulting list is created. Python only prepars "the possibility to do the computations". In the upcoming examples we'll see what does this sentence really mean, for now let's see what do we have in this example: `double_numbers` contains a **map object**, but when you iterate
over it using the `for num in double_numbers` expression you get the expected values.


{% embed include file="src/examples/functional/map.py" %}

**Output:**

{% embed include file="src/examples/functional/map.out" %}


