# Macros
{id: macros}


## What is a macro
{id: what-is-a-macro}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* Metaprogramming - a program that generate a program

* [List of macros](https://doc.rust-lang.org/std/#macros)
* [Macros in the reference](https://doc.rust-lang.org/reference/macros.html)
* [The Little book of Rust Macros](https://veykril.github.io/tlborm/)

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

## macro to say hello
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


## Macro to say hello many times
{id: macro-say-hello-many-times}
{i: macro_rules!}
{i: expr}
{i: "*"}
{i: "+"}

* This macro can accept 0 or more parameters and then it will repeate the code as many times as parameters we got.
* Instead of `*` we could use `+` in the declaration and that would mean the macro accepts 1 or more parameters.

![](examples/macros/say-hello-many-times/src/main.rs)
![](examples/macros/say-hello-many-times/out.out)

## Macro to create a HashMap to be a counter
{id: macro-to-crate-a-hashmap}
{i: HashMap}

![](examples/macros/create-counter-hash/src/main.rs)
![](examples/macros/create-counter-hash/out.out)


## HTML to string macro
{id: html-to-string-macro}

* [html-to-string-macro](https://crates.io/crates/html-to-string-macro)

![](examples/macros/embed-html/Cargo.toml)
![](examples/macros/embed-html/src/main.rs)

## Num traits
{id: num-traits}


* [num-traits](https://crates.io/crates/num-traits)
* [num-traits](https://docs.rs/num-traits)

## Procedural macros
{id: procedural-macros}
{i: proc-macro}
{i: TokenStream}

* [procedural macros](https://doc.rust-lang.org/reference/procedural-macros.html)

* Add `proc-macro` to the `Cargo.toml`

* Here we show that the macro is executed during the compilation.
* It needs to return a TokenStream.

![](examples/macros/hello-world-macro/Cargo.toml)
![](examples/macros/hello-world-macro/src/lib.rs)

![](examples/macros/hello-world-use/Cargo.toml)
![](examples/macros/hello-world-use/src/main.rs)


## Compile random number in the code using macro
{id: compile-random-number-on-the-code}

![](examples/macros/random-constant-macro/Cargo.toml)
![](examples/macros/random-constant-macro/src/lib.rs)

![](examples/macros/random-constant/Cargo.toml)
![](examples/macros/random-constant/src/main.rs)

TODO: #[macro_export]

