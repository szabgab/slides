# STDIN
{id: stdin}

## Variables are immutable by default
{id: variables-are-immutable}
{i: let}

* Variables are immutable by default

![](examples/stdin/immutable_string.rs)
![](examples/stdin/immutable_string.out)

## String in a mutable variable
{id: rust-string-in-mutable-variable}
{i: let}
{i: mut}

* Use the `mut` keyword to mark a variable as mutable.

![](examples/stdin/mutable_string.rs)
![](examples/stdin/mutable_string.out)

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

## Redeclare immutable variable - Shadowing
{id: rust-redeclared-immutable-variable}
{i: let}

![](examples/stdin/shadow.rs)
![](examples/stdin/shadow.out)

## Redeclare immutable variable and change type - Shadowing
{id: rust-redeclared-immutable-variable-change-type}
{i: let}

* When shadowing we can also change the type of the variable.
* e.g. we read from a file or from STDIN a string that we then convert to a number. We can use the same variable name.

![](examples/stdin/change_type.rs)
![](examples/stdin/change_type.out)

## Conditional: if
{id: rust-conditional-if}
{i: if}

![](examples/intro/if.rs)

## Conditional: if - else
{id: rust-conditional-if-else}

![](examples/intro/if_else.rs)

## Command line arguments - argv
{id: command-line-arguments}
{i: argv}

![](examples/intro/argv.rs)

## Rust rectangle ARGV
{id: rust-rectangle}

![](examples/intro/rectangle_argv.rs)

## Variable Scope in Rust
{id: rust-variable-scope}

* Every block creates a scope

![](examples/intro/scope.rs)
![](examples/intro/scope.out)

## Rust constants
{id: rust-constants}
{i: const}

* Value that can be computed during compilation.
* Cannot be changed.
* Must have type declaration.
* Should be `UPPER_CASE`.

![](examples/intro/constant.rs)


## Numerical operations (integers)
{id: numerical-operations-integers}

![](examples/intro/calc.rs)


## Increment integers
{id: increment-integers}

![](examples/intro/increment.rs)



![](examples/intro/small_integers_unfit_in_i8.rs)
![](examples/intro/small_integers_unfit_in_i8.out)

![](examples/intro/increment_small_integers.rs)
![](examples/intro/increment_small_integers.out)


## Declare empty variable - requires type
{id: declare-empty-variable}

![](examples/intro/empty_string.rs)
![](examples/intro/empty_string.out)

## Number in a mutable variables
{id: rust-number-in-mutable-variables}
{i: let}
{i: mut}

![](examples/stdin/number_mutable.rs)
![](examples/stdin/number_mutable.out)


