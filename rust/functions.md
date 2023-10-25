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

## Rust function return value (integer i32)
{id: rust-function-return-value}
{i: return}
{i: i32}

* After an arrow `->` we can add the type of the return value.
* We can then return that value by using the `return` statement.
* `#[allow(clippy::needless_return)]` is there to silence clippy, the linter.

![](examples/functions/return-integer/src/main.rs)

## Return the last expression (no return)
{id: return-the-last-expression}

* If the last thing in the function is an expression (no semi-colon at the end) then this is the returned value.
* No need for the `return` statement.

![](examples/functions/return-integer-expression/src/main.rs)
![](examples/functions/return-integer-expression/out.out)

## Return a string
{id: return-a-string}
{i: String}

![](examples/functions/return-string/src/main.rs)

## Rust recursive functions: factorial
{id: rust-recursive-functions-factorial}

![](examples/functions/factorial/src/main.rs)
![](examples/functions/factorial/out.out)

## Rust recursive functions: Fibonacci
{id: rust-recursive-functions-fibonacci}

![](examples/functions/fibonacci/src/main.rs)

## Make function argument mutable inside the function
{id: make-function-argument-mutable-inside-the-function}
{i: mut}

* Sometimes you pass an argument and you would like to change that value inside the function (without chaning the external variable).

![](examples/functions/change-argument-inside-function/src/main.rs)
![](examples/functions/change-argument-inside-function/out.out)

## Cannot decalre the same function twice
{id: cannot-declare-the-same-function-name-twice}

![](examples/functions/declare-twice/src/main.rs)
![](examples/functions/declare-twice/out.out)

## Expressions vs statements
{id: expressions-vs-statement}

* Expressions have a return value do NOT need a trailing semi-colon
* Statements do not have values and need a semi-colon

![](examples/functions/statements.rs)

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

