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


