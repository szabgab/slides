# Introduction to Rust
{id: rust-intro}


## Rust resources
{id: rust-resources}

* [Rust the language](https://www.rust-lang.org/)
* [Rust Documentation](https://doc.rust-lang.org/)

## Rust Books
{id: rust-books}


* [Learn Rust](https://www.rust-lang.org/learn)
* [The Rust book](https://doc.rust-lang.org/book/)
* [Rust by example](https://doc.rust-lang.org/stable/rust-by-example/)

## Crates
{id: crates-io}

* [Crates.io](https://crates.io/)
* [Docs.rs](https://docs.rs/)
* [Lib.rs](https://lib.rs/) - Lightweight, opinionated, curated, unofficial alternative to crates.io
* [Rust Digger](https://rust-digger.code-maven.com/) - analyzing crates and recommending improvements

## Rust exercises with feedback
{id: rust-exercises-with-feedback}

* [rustlings](https://rustlings.cool/)
* [Exercism Rust track](https://exercism.org/tracks/rust)
* [Rust users forum](https://users.rust-lang.org/)

## Podcast, newsleter
{id: rust-podcast}

* [This week in Rust](https://this-week-in-rust.org/) - a weekly newsletter
* [Rustacean](https://www.rustaceans.org/)
* [Rustacean station](https://rustacean-station.org/) - a podcast


## Other Rust learning resources
{id: other-rust-learning-resources}

* [Let's Get Rusty](https://letsgetrusty.com/)
* [noboilerplate](https://github.com/0atman/noboilerplate)
* [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/)
* [Rust Atomics and Locks](https://marabos.nl/atomics/) Low-Level Concurrency in Practice by Mara Bos



## Rust in other languages
{id: rust-in-other-languages}

* [From Perl to Rust](https://oylenshpeegul.gitlab.io/from-perl-to-rust/introduction.html)

* [The Rust book in Hebrew](https://github.com/IttayWeiss/rustbook-heb)

## Articles about Rust
{id: articles-about-rust}

* [Why do Programmers Love Rust?](https://www.youtube.com/watch?v=vBsEF-anSLY) presentation by Dave Rolsky [slides](https://presentations.houseabsolute.com/why-do-programmers-love-rust/) - [source](https://github.com/autarch/presentations/tree/master/why-do-programmers-love-rust)
* [Why the developers who use Rust love it so much](https://stackoverflow.blog/2020/06/05/why-the-developers-who-use-rust-love-it-so-much/)

## What is written in Rust?
{id: what-is-written-in-rust}

* [Pydentic](https://docs.pydantic.dev/) is now written in Rust.
* [SurrealDB](https://surrealdb.com/) multi-model database.
* ...


## Demo None handling
{id: demo-none-handling}
{i: Option}
{i: match}
{i: Some}
{i: None}

![](examples/intro/demo-none-handling/src/main.rs)


See original idea on [What is Rust and why is it so popular?](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/)


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

![](examples/intro/hello/src/main.rs)

```
rustc src/main.rs
```

```
./main
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

![](examples/intro/hello-world/src/main.rs)
![](examples/intro/hello-world/Cargo.toml)

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

![](examples/intro/comments/src/main.rs)

## Rust - Hello Foo
{id: hello-foo}
{i: let}

![](examples/intro/hello-foo/src/main.rs)
![](examples/intro/hello-foo/out.out)

* [format macro](https://doc.rust-lang.org/std/fmt/)

## Interpolation
{id: string-interpolation}

Since Rust 1.58

![](examples/intro/interpolation/src/main.rs)
![](examples/intro/interpolation/out.out)

## Printing a string
{id: printing-a-string}

![](examples/intro/formatting-required/src/main.rs)
![](examples/intro/formatting-required/out.out)

## Printing a string fixed
{id: printing-a-string-fixed}

![](examples/intro/formatting-required-fixed/src/main.rs)
![](examples/intro/formatting-required-fixed/out.out)

## Debugging print
{id: debugging-print}
{i: dbg!}

* goes to STDERR

![](examples/intro/debugging-print/src/main.rs)
![](examples/intro/debugging-print/out.out)

## Rust and print
{id: rust-and-print}
{i: print!}
{i: println!}
{i: eprint!}
{i: eprintln!}
{i: dbg!}
{i: format!}


* [print!](https://doc.rust-lang.org/std/macro.print.html)    to STDOUT
* [println!](https://doc.rust-lang.org/std/macro.println.html)  to STDOUT

* [eprint!](https://doc.rust-lang.org/std/macro.eprint.html)   to STDERR
* [eprintln!](https://doc.rust-lang.org/std/macro.eprintln.html) to STDERR
* [dbg!](https://doc.rust-lang.org/std/macro.dbg.html)      to STDERR

* [format!](https://doc.rust-lang.org/std/macro.format.html)   returns formatted string

![](examples/intro/print/src/main.rs)
![](examples/intro/print/out.out)


## Exercise 1
{id: exercise-1}

* Make sure you have Rust installed.
* Try `rustc --version`
* Create a new project with Cargo.
* Write a program that prints "Hello World".
* Add comments.

