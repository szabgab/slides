# STDIN
{id: stdin}

## Rust - read input from STDIN
{id: rust-hello-name}
{i: std::io}
{i: String}
{i: stdin}
{i: read_line}
{i: expect}

* Module [std::io](https://doc.rust-lang.org/std/io/)
* [String::new()](https://doc.rust-lang.org/std/string/struct.String.html#method.new) - Creates a new mutable empty string
* `&mut name` passes a reference of the variable to the function as mutable variable. `&` indicates it is a reference.
* `read_line` reads a line from the command line

![](examples/stdin/hello-name/src/main.rs)

![](examples/stdin/hello-name/out.out)

Two problems:
* The response looks broken. It has a newline after the name.
* After the prompt the program waits on a new line.

## Rust - read STDIN - remove trailing newline (trim, chomp)
{id: rust-read-stdin-chomp}
{i: trim_end}
{i: to_string}

* [trim_end](https://doc.rust-lang.org/std/string/struct.String.html#method.trim_end) removes trailing whitespace.
* `to_string` Converts the String to be able to assign to `name` again

![](examples/stdin/hello-name-chomp/src/main.rs)

## Rust - flush STDOUT - read STDIN
{id: rust-flush-stdout-read-stdin-chomp}
{i: print!}

* We use `print!` and not `println!`
* `use std::io::Write;` adds the `flush`

![](examples/stdin/hello-name-chomp-flush/src/main.rs)

## Get number from STDIN
{id: get-number-from-stdin}

![](examples/stdin/get-number-from-stdin/src/main.rs)

## Get number from STDIN - same variable
{id: get-number-from-stdin-same-variable}

![](examples/stdin/get-number-from-stdin-same-variable/src/main.rs)

## Get number (i32) in using a function
{id: get-number-using-function}

* We have not learned functions yet, but in order to make it easier to copy paste this example later we have a solution here

![](examples/stdin/get-number-function/src/main.rs)

## Exercise: STDIN rectangle
{id: exercise-stdin-rectangle}

* Ask the use for the length and the width of a rectangle and print the area and the circumference to the screen.

## Exercis: STDIN calculator
{id: exercise-stdin-calculator}

* The program will ask the user for a number, and for an operator(+, -, /, *) and for another number.
* It will then do the appropriate mathematical operation and print the result.

## Solution STDIN rectangle
{id: solution-stdin-rectangle}

![](examples/stdin/rectangle/src/main.rs)

## Solution: STDIN calculator
{id: solution-stdin-calculator}

![](examples/stdin/calc-stdin/src/main.rs)

