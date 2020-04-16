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


## Variadic function (arbitrary number of parameters)
{id: variadic-function}

* unknown number of parameters
* [variadic functions](https://medium.com/rungo/variadic-function-in-go-5d9b23f4c01a)

![](examples/function-sum/sum_function.go)


## Multiple return values
{id: multiple-return-values}

![](examples/function-multiple-return/multiple_return_function.go)

## Returning an error from a functions
{id: returning-an-error-from-a-function}

![](examples/function-return-error/return_error.go)


## Passing a function as a parameter - Callback function
{id: callback-function}

As it is right now, the `run` function can only accept callback functions without any parameter

![](examples/callback-function/callback_function.go)


## Callback function with one parameter
{id: callback-function-with-one-parameter}


![](examples/callback-function-param/callback_function_param.go)


## Anonymous functions
{id: anonimous-function}

![](examples/function-anonimous/anonymous_function.go)


## Numbers are passed by value
{id: numbers-pass-by-value}

![](examples/function-increment/function_increment.go)
![](examples/function-increment/function_increment.out)

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

## Exercise: Fibonacci
{id: exercise-fibonacci}

Implement a function that accepts a positive integer (n) and returns the n-th numbers of the Fibonacci series.

## Exercise: Defer remove temporary directory
{id: exercise-defer-remove-temporary-directory}

## Exercise: FizzBuzz in function
{id: exercise-fizzbuzz-in-function}

Write a function that given a number will print the number itself or something else according to these rules:
* For multiples of 3 print "Fizz" instead of the number.
* For multiples of 5 print "Buzz".
* For numbers which are multiples of both three and five print "FizzBuzz".

 that prints the numbers from 1 to 100.


Expected output:

![](examples/fizzbuzz-main/fizzbuzz_main.out)


## Solution: FizzBuzz in function
{id: solution-fizzbuzz-in-function}

![](examples/fizzbuzz/fizzbuzz.go)

![](examples/fizzbuzz/fizzbuzz_test.go)

