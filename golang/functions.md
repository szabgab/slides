# Functions
{id: functions}

## Create hello function
{id: hello-function}
{i: func}

![](examples/go-functions/hello_foo_function.go)
![](examples/go-functions/hello_foo_function.out)


## Function with return value
{id: function-sith-return}
{i: return}

![](examples/function-return/comp.go)

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

## Exercise: Fibonacci
{id: exercise-fibonacci}

Implement a function that accepts a positive integer (n) and prints out the first n numbers of the Fibonacci series.

## Solution: Fibonacci
{id: solution-fibonacci}

![](examples/fibonacci/fibonacci.go)

## Solution: Fibonacci recursive
{id: solution-fibonacci-recursive}

![](examples/fibonacci-recursive/fibonacci-recursive.go)



## Exit early with exit code
{id: exit-early}

![](examples/exit/code.go)

```
echo $0
echo %ERRORLEVEL%
```

## Read from stdin (keyboard)
{id: read-from-stdin}

Read from the stdin (standard input) Get input from the keyboard in golang

![](examples/read-from-stdin/read_from_stdin.go)

## Read from stdin (keyboard) with error handling
{id: read-from-stdin-with-error-handling}

![](examples/read-from-stdin-with-error-handling/read_from_stdin_with_error_handling.go)



## get variable type - %T or reflect.TypeOf
{id: get-variable-type}

![](examples/get-type/get-type.go)



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

## Solution: rectangular (STDIN)
{id: solution-rectangular-stdin}

![](examples/rectangular-stdin/rectangular.go)



## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/single-counter.go)


## Logging
{id: logging}

![](examples/logging/logger.go)

* There is a default prefix for each log message
* We can change this prefix using SetFlags
* By default log prints to STDERR (Standard Error)
* Fatal prints the message and exits the script with exit code 1

```
First
2019/10/08 23:47:13 First log
2019/10/08 23:47:13 0x490ef0
2019/10/08 23:47:13 logger.go:14: After setting flags
2019/10/08 23:47:13 logger.go:15: Oups
exit status 1
```

## Logging to a file
{id: logging-to-a-file}

* Set the output filehandle using `SetOutput`

![](examples/log-to-file/log2file.go)

* TODO: log levels?
* TODO: log function names



## Reverse Polish Calculator
{id: reverse-polish-calculator}

* TODO: finish this

![](examples/rpc/rpc.go)


## variadic function
{id: variadic-function}

* unknown number of parameters
* [variadic functions](https://medium.com/rungo/variadic-function-in-go-5d9b23f4c01a)

## multiple return values
{id: multiple-return-values}


## Returning an error from a functions
{id: returning-an-error-from-a-function}
