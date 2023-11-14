# Macros
{id: macros}


## What is a macro
{id: what-is-a-macro}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* Metaprogramming - a program that generate a program

* [List of macros](https://doc.rust-lang.org/std/#macros)
* [Macros in the reference](https://doc.rust-lang.org/reference/macros.html)

* print!
* println!
* vec!

## todo!
{id: macro-todo}
{i: todo!}
{i: unimplemented!}

* [todo!](https://doc.rust-lang.org/std/macro.todo.html) when we put in the layout of the code but cannot work on all the codepathes at the same time and we would like to say it explicitely.
* [unimplemented!](https://doc.rust-lang.org/std/macro.unimplemented.html)

![](examples/macros/todo/src/main.rs)

```
cargo run foo
cargo run bar
```

## Declarative macros
{id: declarative-macros}

DSL - Domain Specific Language

## Hello World macro
{id: macro-hello-world}
{i: macro_rules!}

![](examples/macros/hello-world/src/main.rs)

## Say hello macro
{id: macro-say-hello}
{i: macro_rules!}
{i: expr}

* name of the macro
* parameters of the macro
* `$name: expr`    means we have a parameter called `$name` and it has a type "expr" (expression)


// $t:ty          means we have a paramerer called $t    and it has a type "ty" (type, such as i32 or f64)
// With this macro we can replace a short syntax with a longer syntax in at compile time.

//maco_rules! include_text_file {
//}


![](examples/macros/say-hello/src/main.rs)

## HTML to string macro
{id: html-to-string-macro}

* [html-to-string-macro](https://crates.io/crates/html-to-string-macro)

![](examples/macros/embed-html/Cargo.toml)
![](examples/macros/embed-html/src/main.rs)

## Num traits
{id: num-traits}


* [num-traits](https://crates.io/crates/num-traits)
* [num-traits](https://docs.rs/num-traits)


