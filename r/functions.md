# Functions
{id: functions}

## Functions overview
{id: functions-overview}

```
function_name = function(arg1, arg2, arg3) {
     # commands
     return(someReturnValue)
}
```

* Function parameter names are local to the function
* variables created in the function are local
* Result of last expression returned implicitely (even without calling return())

* When accepting a vector of numbers what if the user sends in a vector of strings (different class of data)?
* What if some of the values are missing? (NA)
* What if the vector is empty?

## Simple add function
{id: simple-add-function}

![](examples/functions/rectangle_area_function.R)

![](examples/functions/distance_function.R)


## Recursive Fibonacci
{id: recursive-fibonacci}

![](examples/functions/fibonacci_recursive.R)

## Fibonacci
{id: fibonacci}

![](examples/functions/fibonacci.R)
