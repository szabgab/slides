# Functions
{id: functions}

## Hello World function
{id: hello-world-function}
{i: func}

![](examples/function-hello-world/hello_world_function.go)


## Hello You function (passing parameter)
{id: hello-you-function}
{i: func}

![](examples/go-functions/hello_foo_function.go)
![](examples/go-functions/hello_foo_function.out)


## Function with return value
{id: function-sith-return}
{i: return}

![](examples/function-return/add_function.go)


## variadic function
{id: variadic-function}

* unknown number of parameters
* [variadic functions](https://medium.com/rungo/variadic-function-in-go-5d9b23f4c01a)

![](examples/function-sum/sum_function.go)


## multiple return values
{id: multiple-return-values}


## Returning an error from a functions
{id: returning-an-error-from-a-function}


## Callback function
{id: callback-function}

As it is right now, the `run` function can only accept callback functions without any parameter

![](examples/callback-function/callback_function.go)


## Callback function with one parameter
{id: callback-function-with-one-parameter}


![](examples/callback-function-param/callback_function_param.go)



## Variable declaration outside of functions
{id: variable-declaration-outside-of-functions}

![](examples/variable-declaration/declaration.go)

```
// var i int
// i = 42

// var i int = 42
// i := 42   // (is the same but this one cannot be used on the package level

// var (
//    i = 42
//    j = 23
// )
```


## Defer
{id: defer}
{i: defer}


Every `defer` statement is executed after the enclosing function ends.
In reverse order. (Similar to `END` block in Perl, similar to `with` context in python)

![](examples/defer/defer.go)

```
$ go run defer.go

first
second
third
two
one
```

## Deferred cd in a function
{id: deferred-cd-in-a-function}

![](examples/cd-and-back/deferred_cd.go)


## Defer does not work in if-statements
{id: defer-not-in-if}

![](examples/defer-no-in-if/defer_no_in_if.go)


## Defer and parameters
{id: defer-with-parameters}

![](examples/defer-and-parameters/defer_and_parameters.go)

* The deffered function will see the its parameter when we defer the function not when it is executed


## Defer and slice
{id: defer-and-slice}

![](examples/defer-and-slice/defer_and_slice.go)


## TODO: Defer remove temporary directory
{id: defer-remove-temporary-directory}


## Exercise: Fibonacci
{id: exercise-fibonacci}

Implement a function that accepts a positive integer (n) and prints out the first n numbers of the Fibonacci series.

## Solution: Fibonacci
{id: solution-fibonacci}

![](examples/fibonacci/fibonacci.go)

## Solution: Fibonacci recursive
{id: solution-fibonacci-recursive}

![](examples/fibonacci-recursive/fibonacci-recursive.go)





## Solution: rectangular (STDIN)
{id: solution-rectangular-stdin}

![](examples/rectangular-stdin/rectangular.go)



## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/single-counter.go)



