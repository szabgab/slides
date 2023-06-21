# STDIN
{id: stdin}

## Hello World in (immutable) variable
{id: rust-hello-world-in-immutable-variable}
{i: let}

* Variables are by default immutable

![](examples/stdin/hello_world_in_immutable_variable.rs)
![](examples/stdin/hello_world_in_immutable_variable.out)

## String in mutable variable
{id: rust-string-in-mutable-variable}
{i: let}
{i: mut}

![](examples/stdin/hello_world_in_mutable_variable.rs)
![](examples/stdin/hello_world_in_mutable_variable.out)

## Rust number in mutable variables
{id: rust-number-in-mutable-variables}
{i: let}
{i: mut}

![](examples/stdin/number_mutable.rs)
![](examples/stdin/number_mutable.out)

## Rust - Hello name - input from STDIN
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
* The response is broken. It has a newline after the name.
* After the prompt the program waits on a new line.

## Rust - read STDIN - chomp - remove trailing newline
{id: rust-read-stdin-chomp}
{i: trim_end}

* [trim_end](https://doc.rust-lang.org/std/string/struct.String.html#method.trim_end) removes trailing whitespace.
* `to_string` Converts the String to be able to assign to `name` again

![](examples/stdin/hello_name_chomp.rs)

## Rust - flush STDOUT - read STDIN - chomp
{id: rust-flush-stdout-read-stdin-chomp}

* `use std::io::Write;` adds the `flush`

![](examples/stdin/hello_name_chomp_flush.rs)


## Hello World in redeclared immutable variable - shadowed
{id: rust-hello-world-in-redeclared-immutable-variable}
{i: let}
{i: mut}

* When shadowing we can also change the type of the variable.
* e.g. we read from a file or from STDIN a string that we then convert to a number. We can use the same variable name.

![](examples/intro/hello_world_in_redeclared_immutable_variable.rs)

![](examples/intro/shadow.rs)

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

![](examples/strings/string_to_float.rs)

## Declare empty variable - requires type
{id: declare-empty-variable}

![](examples/intro/empty_string.rs)
![](examples/intro/empty_string.out)


