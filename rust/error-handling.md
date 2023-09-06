# Error handling in Rust
{id: error-handling}


## Runtime error (panic) noticed during compilation.
{id: runtime-panic-noticed-during-compilation}

![](examples/errors/div_by_zero_hard_coded.rs)
![](examples/errors/div_by_zero_hard_coded.out)

## Divide by zero panick in function
{id: panick-in-function}

![](examples/errors/divide_by_zero_panick.rs)

## Return error on failure
{id: return-error-on-failure}

![](examples/errors/divide_by_zero_return_error.rs)


## Divide by zero runtime panic
{id: divide-by-zero-runtime-panic}

![](examples/errors/div_by_zero.rs)
![](examples/errors/div_by_zero.out)

## Divide by zero return error
{id: divide-by-zero-return-error}

![](examples/errors/div_by_zero_catch_error.rs)

## factorial function, runtime panic
{id: factorial-function-runtime-panic}
{i: panic!}

* In this series of examples we'll see how a function we write can report error and how the caller can handle the error.
* In the first example we implement a function to calculate factorial recursively. The specific task is not important, just that if the user supplies a negative number then this code will crash. More precisely, it will have a panic when our program reaches stack overflow.

![](examples/errors/factorial.rs)
![](examples/errors/factorial.out)

## factorial create panic
{id: factorial-create-panic}

In order to avoid this stack overflow our function needs to check the input and then if it is a negative number then report it.
(I know, instead of i64 we could have used u64 which is an unsigned integer that would only allow non-negative numbers. but in other functions we might not be able to use the type-system for that. e.g. what if we expect a positive whole number larger than 2?

One way to avoid reaching stack overflow is to call panic! ourselves.

![](examples/errors/factorial_create_panic.rs)
![](examples/errors/factorial_create_panic.out)

## Out of bound for vectors
{id: out-of-bound-for-vectors}

* Run-time panic

![](examples/errors/out_of_bounds_vector.rs)
![](examples/errors/out_of_bounds_vector.out)

## Out of bound for arrays
{id: out-of-bound-for-arrays}

* Compile-time panic

![](examples/errors/out_of_bounds_array.rs)
![](examples/errors/out_of_bounds_array.out)

## Open files
{id: open-files}

![](examples/errors/file_open.rs)

## Error handling on the command line
{id: command-line-error-handling}

![](examples/argv-error-handling/src/main.rs)

