# Functions
{id: functions}

## Rust main function
{id: rust-main-function}
{i: fn}
{i: main}

* There are two types of crates: Libraries and executables. The latter can also contain libraries.
* For executable crates we must have a file called `src/main.rs` and it must have a function called `main`
* This is the most basic definition of a `main` function. It does nothing.

![](examples/functions/main/src/main.rs)

## Rust hello world function
{id: rust-hello-world-function}
{i: fn}

* We can declare functions with other names using the `fn` keyword.
* The relative location of the functions does not matter. There is no need to defined headers.

![](examples/functions/hello-world/src/main.rs)

## Rust function with parameter (&str)
{id: rust-function-with-parameter}
{i: &str}

* Functions can expect parameters.
* We have to define the type of the parameter.
* In this case we are expecting a [string slice](https://doc.rust-lang.org/std/primitive.str.html) `&str`.
* If we already have a string slice we can pass it as it is.
* If we have a [String](https://doc.rust-lang.org/std/string/struct.String.html) then we have to prefix it with `&`.

![](examples/functions/hello-foo/src/main.rs)
![](examples/functions/hello-foo/out.out)

## Rust function return value
{id: rust-function-return-value}

![](examples/functions/return.rs)

## Rust recursive functions: factorial
{id: rust-recursive-functions-factorial}

![](examples/functions/factorial.rs)

## rust recursive functions: Fibonacci
{id: rust-recursive-functions-fibonacci}

![](examples/functions/recursive_fibonacci.rs)

## Make function argument mutable inside the function
{id: make-function-argument-mutable-inside-the-function}

![](examples/functions/change_argument_inside_function.rs)

## Cannot decalre the same function twice
{id: cannot-declare-the-same-function-name-twice}

![](examples/functions/add.rs)

## Expressions vs statements
{id: expressions-vs-statement}

* Expressions have a return value do NOT need a trailing semi-colon
* Statements do not have values and need a semi-colon

![](examples/functions/statements.rs)

## Implicit return the last expression
{id: implicit-return-the-last-expression}

![](examples/functions/implicit_return.rs)

## Increment in a function
{id: increment-in-a-function}

![](examples/functions/increment.rs)

## Count digits using functions
{id: count-digits-functions}

![](examples/functions/count_digits.rs)

## Exercise rectangle functions
{id: exercise-rectangle-functions}

In an earlier chapter we had an exercise to ask the use for the length and the width of a rectangle and print the
area and the circumference to the screen.

Simplify it by moving the code that reads the number from STDIN into a function that we call twice. Once for the width and one for the length.

![](examples/functions/rectangle_stdin.rs)

## Function returning multiple values
{id: function-returning-multiple-values}

* returns a tuple

![](examples/functions/return_multiple_values.rs)

## Function accepting multiple types (e.g. any type of numbers)
{id: function-accepting-multiple-types}

![](examples/functions/accepting_multiple_types.rs)

## Function that can accept any number (any integer or any float)
{id: function-to-accept-any-number}

![](examples/functions/any_number/Cargo.toml)
![](examples/functions/any_number/src/main.rs)

