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

![](examples/stdin/hello_name.rs)

![](examples/stdin/hello_name.out)

Two problems:
* The response looks broken. It has a newline after the name.
* After the prompt the program waits on a new line.

## Rust - read STDIN - remove trailing newline (trim, chomp)
{id: rust-read-stdin-chomp}
{i: trim_end}
{i: to_string}

* [trim_end](https://doc.rust-lang.org/std/string/struct.String.html#method.trim_end) removes trailing whitespace.
* `to_string` Converts the String to be able to assign to `name` again

![](examples/stdin/hello_name_chomp.rs)

## Rust - flush STDOUT - read STDIN
{id: rust-flush-stdout-read-stdin-chomp}
{i: print!}

* We use `print!` and not `println!`
* `use std::io::Write;` adds the `flush`

![](examples/stdin/hello_name_chomp_flush.rs)

## Convert string to (integer) number
{id: rust-convert-string-to-number}
{i: i32}
{i: parse}
{i: expect}

* In the printing we won't see the difference, but we can do numberical operations on numbers

![](examples/stdin/string_to_int.rs)
![](examples/stdin/string_to_int.out)

## Convert string to number that ends with newline
{id: rust-convert-string-to-number-end-with-newline}
{i: trim}

![](examples/stdin/string_to_int_fail.rs)
![](examples/stdin/string_to_int_fail.out)

## Convert string to number after removing whitespaces
{id: rust-convert-string-to-number-trim}
{i: trim}

![](examples/stdin/string_to_int_trim.rs)
![](examples/stdin/string_to_int_trim.out)

## Convert string to float
{id: convert-string-to-float}
{i: f32}

* Sometimes we are expecting floating point numbers.

![](examples/stdin/string_to_float.rs)
![](examples/stdin/string_to_float.out)

## Get number from STDIN
{id: get-number-from-stdin}

![](examples/stdin/get_number_from_stdin.rs)

## Get number from STDIN - same variable
{id: get-number-from-stdin-same-variable}

![](examples/stdin/get_number_from_stdin_same_variable.rs)

## Variable Scope in Rust
{id: rust-variable-scope}

* Every block creates a scope

![](examples/intro/scope.rs)
![](examples/intro/scope.out)

## Declare empty variable - requires type
{id: declare-empty-variable}

![](examples/intro/empty_string.rs)
![](examples/intro/empty_string.out)

## Exercise STDIN rectangle
{id: exercise-stdin-rectangle}

* Ask the use for the length and the width of a rectangle and print the area and the circumference to the screen.

## Solution STDIN rectangle
{id: solution-stdin-rectangle}

![](examples/stdin/rectangle.rs)

