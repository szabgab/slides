# Functions
{id: functions}

## Hello World function
{id: hello-world-function}
{i: func}

![](examples/function-hello-world/hello_world_function.go)
![](examples/function-hello-world/hello_world_function.out)


## Hello You function (passing parameter)
{id: hello-you-function}
{i: func}

![](examples/go-functions/hello_foo_function.go)
![](examples/go-functions/hello_foo_function.out)

## Function with multiple parameters
{id: function-with-multiple-parameters}

![](examples/print-substring-function/print_substring_function.go)
![](examples/print-substring-function/print_substring_function.out)

## Function with return value
{id: function-sith-return}
{i: return}

![](examples/function-return/function_return.go)
![](examples/function-return/function_return.out)


## Multiple return values
{id: multiple-return-values}

![](examples/function-multiple-return/multiple_return_function.go)
![](examples/function-multiple-return/multiple_return_function.out)

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
![](examples/function-anonimous/anonymous_function.out)

## Anonymous functions assigned to name
{id: anonimous-function-assigned-to-name}

![](examples/anonymous-function-with-name/anonymous_function_with_name.go)
![](examples/anonymous-function-with-name/anonymous_function_with_name.out)


## Numbers are passed by value
{id: numbers-pass-by-value}

![](examples/function-increment/function_increment.go)
![](examples/function-increment/function_increment.out)

## Function Overloading - Multiple function with the same name
{id: multiple-function-with-the-same-name}

* There is no function overloading in Golang

![](examples/redeclare-function/redeclare_function.go)
![](examples/redeclare-function/redeclare_function.out)


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


## Defer in if-statements 
{id: defer-in-if}

* Even if we put the defer call inside an if-statement, the deferred function will only execute at the end of the enclosing function.

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

Write a function that will create a temporary directory and then it will remove it once the function is done.
Make sure the directory is removed no matter how you exit from the function.

![](examples/remove-temp-directory/remove_temp_directory.go)

## Exercise: FizzBuzz in function
{id: exercise-fizzbuzz-in-function}

Write a function that given a number will print the number itself or something else according to these rules:
* For multiples of 3 print "Fizz" instead of the number.
* For multiples of 5 print "Buzz".
* For numbers which are multiples of both three and five print "FizzBuzz".

 that prints the numbers from 1 to 100.


Expected output:

![](examples/fizzbuzz-main/fizzbuzz_main.out)


## Exercise: ROT13
{id: exercise-rot13}

Implement a function that given a string will return its [](https://en.wikipedia.org/wiki/ROT13) encryption
and given the encrypted string will return the original string. Characters that are not letters
will remain the same.

e.g. "hello World!" is converted to "Uryyb Jbeyq!"

## Solution: FizzBuzz in function
{id: solution-fizzbuzz-in-function}

![](examples/fizzbuzz/fizzbuzz.go)

![](examples/fizzbuzz/fizzbuzz_test.go)

## Solution: ROT13
{id: solution-rot13}

![](examples/rot13/rot13.go)
