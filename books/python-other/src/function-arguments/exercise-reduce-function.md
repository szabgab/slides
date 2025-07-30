# Exercise: implement the reduce function

```
my_reduce(function, a, b, c, ...)
```

* 'function' is expected to be a function that receives two arguments and returns a result.
* If only the function is given, return None.
* If only one value is given, return that value.
* Take the first two values, run the function on them.  Then take the result and the next value and run the function on them. etc.  When no more values are left, return the last result.

{% embed include file="src/examples/function-arguments/my_reduce_skeleton.py" %}







