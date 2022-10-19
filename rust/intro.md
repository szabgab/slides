# Rust intro
{id: rust-intro}

## Rust resources
{id: rust-resources}

* [From Perl to Rust](https://oylenshpeegul.gitlab.io/from-perl-to-rust/introduction.html)
* [Rust Documentation](https://doc.rust-lang.org/)
* [Rust the language](https://www.rust-lang.org/)
* [Learn Rust](https://www.rust-lang.org/learn)

## Install Rust
{id: rust-installation}


## Hello World
{id: rust-hello-world}

![](examples/intro/hello.rs)

```
rustc hello.rs
```

```
./hello
```

## Hello World with Cargo
{id: hello-world-with-cargo}

```
cargo new hello
cd hello
cargo run
```

## My little Rust runner
{id: my-little-rust-runner}

This is especially usefule for the slides so I can create individual Rust example files and run them stand alone

![](rust)


## Rust and print
{id: rust-and-print}

```
print!
println!
eprint!   to STDERR
eprintln! to STDERR

format!
```

## Rust and comments
{id: rust-comments}
{i: //}

* Both single-line and multi-line comments are available in Rust

![](examples/intro/comments.rs)


## Hello Foo
{id: hello-foo}

![](examples/intro/hello_foo.rs)

* [format macro](https://doc.rust-lang.org/std/fmt/)

## Interpolation
{id: string-interpolation}

Since Rust 1.58

![](examples/intro/interpolation.rs)

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

## While loop in Rust
{id: rust-while-loop}
{i: while}

![](examples/intro/while.rs)

## Infinite loop in Rust with break
{id: rust-infinite-loop}
{i: loop}
{i: break}

![](examples/intro/loop.rs)

## for loop in Rust
{id: rust-for-loop}
{i: for}


* `1..5` mean the right-hand limit is NOT included.
* `1..=5` means the right-hand limit is included

![](examples/intro/for_loop.rs)
![](examples/intro/for_loop.out)

## Variable Scope in Rust
{id: rust-variable-scope}

* Every block creates a scope

![](examples/intro/scope.rs)
![](examples/intro/scope.out)

## Rust Type system
{id: rust-type-system}


## Rust numerical operations
{id: rust-numerical-operations}

![](examples/intro/numerical_operations.rs)

## Rust numerical types
{id: rust-numerical-types}
{i: i32}
{i: i64}

* By default numbers are stored in i32 whose range is -2147483648..=2147483647
* We can explicitely put numbers in different types

![](examples/intro/number_types.rs)

## Rust type mismatch in numerical operation
{id: rust-type-mismatch-in-numerical-operation}

![](examples/intro/type_mismatch.rs)

* TODO: if we remove the i32 then this works even though, I think, the default is i32


## Rust Overflow
{id: rust-overflow}

![](examples/intro/overflow.rs)
![](examples/intro/overflow.out)

## Rust constants
{id: rust-constants}
{i: let}

![](examples/intro/constant.rs)

## Rust mutable variables
{id: rust-variables}
{i: let}
{i: mut}

![](examples/intro/variables.rs)


