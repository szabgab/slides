# Functions 2
{id: functions-2}

## Numbers passed by reference
{id: numbers-pass-by-reference}

![](examples/function-increment-with-pointer/function_increment_with_pointer.go)
![](examples/function-increment-with-pointer/function_increment_with_pointer.out)

## Array passed by value or by reference
{id: array-passed-by-value}

![](examples/function-change-array/function_change_array.go)
![](examples/function-change-array/function_change_array.out)

## Multiple function with the same name
{id: multiple-function-with-the-same-name}

* no, we cannot have such thing in Golang

![](examples/redeclare-function/redeclare_function.go)
![](examples/redeclare-function/redeclare_function.out)

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



## Defer and slice
{id: defer-and-slice}

![](examples/defer-and-slice/defer_and_slice.go)


## Exercise: Fibonacci series
{id: exercise-fibonacci-series}

Implement a function that accepts a positive integer (n) and return the first n numbers of the Fibonacci series.

## Exercise: Permutations
{id: exercise-permutations}

Write a program to print all permutations of a given string

For "ABC", it should print the following series: ABC ACB BAC BCA CBA CAB


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

## Solution: Fibonacci series
{id: solution-fibonacci-series}

![](examples/fibonacci/fibonacci.go)

## Solution: Fibonacci recursive
{id: solution-fibonacci-recursive}

![](examples/fibonacci-recursive/fibonacci_recursive.go)


## Solution: single counter
{id: solution-single-counter}

![](examples/counter-single/counter_single.go)

## Solution: Permutations
{id: solution-permutations}

![](examples/permutations/permutations.go)
![](examples/permutations/permutations_test.go)


## Solution: 100 doors
{id: solution-100-doors}

![](examples/100-doors/100_doors.go)
![](examples/100-doors/100_doors_test.go)

## TODO return array
{id: return-array}

![](examples/return-array/return_array.go)

