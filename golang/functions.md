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


## Multiple return values
{id: multiple-return-values}

![](examples/function-multiple-return/multiple_return_function.go)

## Returning an error from a functions
{id: returning-an-error-from-a-function}

![](examples/function-return-error/return_error.go)


## Callback function
{id: callback-function}

As it is right now, the `run` function can only accept callback functions without any parameter

![](examples/callback-function/callback_function.go)


## Callback function with one parameter
{id: callback-function-with-one-parameter}


![](examples/callback-function-param/callback_function_param.go)


## Anonymous functions
{id: anonimous-function}

![](examples/function-anonimous/anonymous_function.go)


## TODO: pass by value, pass by reference
{id: functions-todo}

* return by value: return variable
* return by reference:  return *variable

* return named value:

func f() (  result int) {
    ...
    return
}

does not seem to be very readable

* Dispatch table

## Methods
{id: methods}

* Functions that run in a context (of a struct)
* [video](https://youtu.be/YS4e4q9oBaU?t=17316)



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

## Exercise: FizzBuzz in function
{id: exercise-fizzbuzz-in-function}

Write a function that given a number will print the number itself or something else according to these rules:
* For multiples of 3 print "Fizz" instead of the number.
* For multiples of 5 print "Buzz".
* For numbers which are multiples of both three and five print "FizzBuzz".

 that prints the numbers from 1 to 100.


Expected output:

![](examples/fizzbuzz-main/fizzbuzz_main.out)


## Exercise: 100 doors
{id: exercise-100-doors}

* There are 100 doors in a row that are all initially closed.
* You make 100 passes by the doors.
* The first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,  close it).
* The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it.
* The third time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door.

Task

* Answer the question:   what state are the doors in after the last pass?   Which are open, which are closed? 

* [Source](https://rosettacode.org/wiki/100_doors)

## Solution: Fibonacci
{id: solution-fibonacci}

![](examples/fibonacci/fibonacci.go)

## Solution: Fibonacci recursive
{id: solution-fibonacci-recursive}

![](examples/fibonacci-recursive/fibonacci_recursive.go)


## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/counter_single.go)


## Solution: FizzBuzz in function
{id: solution-fizzbuzz-in-function}

![](examples/fizzbuzz/fizzbuzz.go)

![](examples/fizzbuzz/fizzbuzz_test.go)

## Solution: 100 doors
{id: solution-100-doors}

![](examples/100-doors/100_doors.go)
![](examples/100-doors/100_doors_test.go)


