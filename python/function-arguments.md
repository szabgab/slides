# Variable number of function arguments
{id: variable-number-function-arguments}

## Python function arguments - a reminder
{id: function-arguments}

* Order of parameter
* Arguments with default values are optional (and come at the end of the definition)
* Number of arguments is know at the time of function definition. The only flexibility is provided by the optional arguments.

![](examples/advanced/function_arguments.py)


## Functions with unknown number of argumerns
{id: function-with-unknown-number-of-arguments}

* sum(a, b, c, ...)
* reduce(function, a, b, c, ...)
* report (function, foo = 23, bar = 19, moo = 70, ...)
* report (function, a, b, c, ..., foo = 23, bar = 19, moo = 70, ...)



## Variable length argument list with * and **
{id: varagrs}
{i: *}
{i: **}
{i: *args}
{i: **kwargs}
![](examples/advanced/varargs.py)
![](examples/advanced/varargs.out)


## Passing arguments as they were received (but incorrectly)
{id: passing-varargs}

What if we need to pass the list of individual arguments (or pairs) to another function?

![](examples/advanced/passing_varargs.py)
![](examples/advanced/passing_varargs.out)

g() received 2 individual parameters, the first was a tuple, the second a dictionary



## Unpacking args before passing them on
{id: unpacking-args}
![](examples/advanced/unpacking_varargs.py)
![](examples/advanced/unpacking_varargs.out)


## Exercise: implement the my_sum function
{id: exercise-sum-function}

* my_sum should be able to accept any number of values and return their sum.
* my_sum() should return 0 or None. Decide yourself!
* my_sum(2, 3) should return 5.  etc.



## Solution: implement the my_sum function
{id: solution-sum-function}
![](examples/advanced/my_sum.py)


## Exercise: implement the reduce function
{id: exercise-reduce-function}

```
my_reduce(function, a, b, c, ...)
```

* 'function' is expected to be a function that receives two arguments and returns a result.
* If only the function is given, return None.
* If only one value is given, return that value.
* Take the first two values, run the function on them.  Then take the result and the next value and run the function on them. etc.  When no more values are left, return the last result.

![](examples/advanced/my_reduce_skeleton.py)


## Soluton: implement the reduce function
{id: solution-reduce-function}
![](examples/advanced/my_reduce.py)


## Exercise: sort pairs
{id: exercise-sort-pairs}


Create a function called sort_pairs, that would receive a sorting method, e.g.
the word 'keys' or the word 'values' and will receive an arbitrary number of key-value pairs
and will return a list of tuples.



```
sort_pairs( 'keys', foo = 23, bar = 47)
[('bar', 47), ('foo', 23)]

sort_pairs( 'values', foo = 23, bar = 47)
[('foo', 23), ('bar', 47)]
```


## Solution: sort pairs
{id: solution-sort-pairs}
![](examples/advanced/sort_pairs.py)



