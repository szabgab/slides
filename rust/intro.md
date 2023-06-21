# Introduction to Rust
{id: rust-intro}

## Rust resources
{id: rust-resources}

* [Learn Rust](https://www.rust-lang.org/learn)
* [The Rust book](https://doc.rust-lang.org/book/)

* [Rust Documentation](https://doc.rust-lang.org/)
* [Rust the language](https://www.rust-lang.org/)

* [From Perl to Rust](https://oylenshpeegul.gitlab.io/from-perl-to-rust/introduction.html)

* [The Rust book in Hebrew](https://github.com/IttayWeiss/rustbook-heb)

## Install Rust
{id: rust-installation}

See in the [Rust book](https://doc.rust-lang.org/stable/book/ch01-01-installation.html)

```
rustup --version

rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.70.0 (90c541806 2023-05-31)`
```

```
rustc --version

rustc 1.70.0 (90c541806 2023-05-31)
```

## Editor and IDE
{id: rust-editor-and-ide}

* Visual Studio Code with the `rust-analyzer` plugin.
* vim


## Hello World
{id: rust-hello-world}
{i: fn}
{i: main}
{i: println!}

* Rust files must have an extension of `.rs`.
* The main Rust file must have a function called `main`.
* `println!` is a macro (it looks like function, it generates some Rust code during compilation).

![](examples/intro/hello.rs)

```
rustc hello.rs
```

```
./hello
```

## Hello World with Cargo
{id: hello-world-with-cargo}
{i: cargo}

* Cargo is the package management system of Rust
* `cargo new hello-world` creates a new folder called `hello-world`
* With a file called `Cargo.toml`
* A folder called `src` and  a file `src/main.rs` with the hello world code.
* `cargo run` will comple the code and run it.

```
cargo new hello-world
cd hello-world
```

![](examples/hello-world/src/main.rs)
![](examples/hello-world/Cargo.toml)

* It will also create a git repository out of this folder.

```
$ cargo run
   Compiling hello-world v0.1.0 (/home/gabor/work/slides/rust/examples/hello-world)
    Finished dev [unoptimized + debuginfo] target(s) in 0.34s
     Running `target/debug/hello-world`
Hello, world!
```

It also created a file called `Cargo.lock` and a folder called `target`.
* `Cargo.lock` is used to fix the versions of all the dependencies of the project. We have none so far.
* `target` contains the compiled file and all the temporay files that Rust needed for the compilation.


## My little Rust runner
{id: my-little-rust-runner}

* This is especially useful for the slides so I can create individual Rust example files and run them stand alone.

![](rust.sh)


```
./rust.sh examples/intro/hello.rs
```


## Rust and comments
{id: rust-comments}
{i: //}
{i: /* */}

* Both single-line and multi-line comments are available in Rust

* [spec of comments](https://doc.rust-lang.org/reference/comments.html)

![](examples/intro/comments.rs)

## Rust - Hello Foo
{id: hello-foo}
{i: let}

![](examples/intro/hello_foo.rs)
![](examples/intro/hello_foo.out)

* [format macro](https://doc.rust-lang.org/std/fmt/)

## Interpolation
{id: string-interpolation}

Since Rust 1.58

![](examples/intro/interpolation.rs)

## Printing a string
{id: printing-a-string}

![](examples/intro/formatting_required.rs)
![](examples/intro/formatting_required.out)

## Printing a string fixed
{id: printing-a-string-fixed}

![](examples/intro/formatting_required_fixed.rs)
![](examples/intro/formatting_required_fixed.out)

## Debugging print
{id: debugging-print}
{i: dbg}

![](examples/intro/debugging_print.rs)
![](examples/intro/debugging_print.out)


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

![](examples/intro/hello_name.rs)

![](examples/intro/hello_name.out)

Two problems:
* The response is broken. It has a newline after the name.
* After the prompt the program waits on a new line.

## Rust - read STDIN - chomp - remove trailing newline
{id: rust-read-stdin-chomp}
{i: trim_end}

* [trim_end](https://doc.rust-lang.org/std/string/struct.String.html#method.trim_end) removes trailing whitespace.
* `to_string` Converts the String to be able to assign to `name` again

![](examples/intro/hello_name_chomp.rs)

## Rust - flush STDOUT - read STDIN - chomp
{id: rust-flush-stdout-read-stdin-chomp}

* `use std::io::Write;` adds the `flush`

![](examples/intro/hello_name_chomp_flush.rs)


## Hello World in (immutable) variable
{id: rust-hello-world-in-immutable-variable}
{i: let}

* Variables are by default immutable

![](examples/intro/hello_world_in_immutable_variable.rs)
![](examples/intro/hello_world_in_immutable_variable.out)

## Hello World in mutable variable
{id: rust-hello-world-in-mutable-variable}
{i: let}
{i: mut}

![](examples/intro/hello_world_in_mutable_variable.rs)

## Hello World in redeclared immutable variable - shadowed
{id: rust-hello-world-in-redeclared-immutable-variable}
{i: let}
{i: mut}

* When shadowing we can also change the type of the variable.
* e.g. we read from a file or from STDIN a string that we then convert to a number. We can use the same variable name.

![](examples/intro/hello_world_in_redeclared_immutable_variable.rs)

![](examples/intro/shadow.rs)

## Macros
{id: macros}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* Metaprogramming - a program that generate a program


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

## Rust mutable variables
{id: rust-variables}
{i: let}
{i: mut}

![](examples/intro/variables.rs)


## Rust rectangle ARGV
{id: rust-rectangle}

![](examples/intro/rectangle_argv.rs)

## Rust and print
{id: rust-and-print}

```
print!
println!
eprint!   to STDERR
eprintln! to STDERR

format!
```

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

