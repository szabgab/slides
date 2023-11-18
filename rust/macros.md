# Macros
{id: macros}


## What is a macro
{id: what-is-a-macro}

Somthing that looks like a function but ends with an exclamation point. e.g. `println!`

* DRY - Don't Repeate Yourself
* Metaprogramming - a program that generate a program
* DSL - Domain Specific Language
* Variadic Interfaces (the same function name but different number of arguments, eg. sum())

* [Macros in the reference](https://doc.rust-lang.org/reference/macros.html)
* [The Little book of Rust Macros](https://veykril.github.io/tlborm/)
* [Macros tutorial](https://blog.logrocket.com/macros-in-rust-a-tutorial-with-examples/)

* [print!](https://doc.rust-lang.org/std/macro.print.html)
* [println!](https://doc.rust-lang.org/std/macro.println.html)
* [vec!](https://doc.rust-lang.org/std/macro.vec.html)
* [todo!](https://doc.rust-lang.org/std/macro.todo.html)
* [include_str!](https://doc.rust-lang.org/std/macro.include_str.html)
* [include_bytes!](https://doc.rust-lang.org/std/macro.include_bytes.html)
* [unimplemented!](https://doc.rust-lang.org/std/macro.unimplemented.html)
* [matches!](https://doc.rust-lang.org/std/macro.matches.html)

* [Full list of standard macros](https://doc.rust-lang.org/std/#macros)
* [Crates tagged as macro](https://crates.io/keywords/macro)

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

* Use `macro_rules!`
* Macros look like functions with an exclamation mark `!` at the end.
* `match`-like arms to match the input of the macro.


## Hello World macro
{id: macro-hello-world}
{i: macro_rules!}

* The name of the macro is `hello_world`
* The `()` matches empty input.

![](examples/macros/hello-world/src/main.rs)

## Macro with parameter to say hello
{id: macro-say-hello}
{i: macro_rules!}
{i: expr}

* The macro is called `say_hello`.
* parameters of the macro
* `$name: expr`    means that the macro is expecting an `expr` (expression) and it will be assigned to a variable called `$name`.


// $t:ty          means we have a paramerer called $t    and it has a type "ty" (type, such as i32 or f64)
// With this macro we can replace a short syntax with a longer syntax in at compile time.


![](examples/macros/say-hello/src/main.rs)

## Macro with optional parameter to say hello
{id: macro-with-optional-parameter}

* In this macro we have two "arms". The first will handle the case when no paramater is passed.
* We can have separate implementations or we can recursively use the macro.

![](examples/macros/say-hello-optional/src/main.rs)


## Macro with many parameters to say hello
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
* Apparently the Macro needs to be in its own Crate separate from where it is being used.

* Add `proc-macro` to the `Cargo.toml`

* Here we show that the macro is executed during the compilation.
* It needs to return a TokenStream.

![](examples/macros/hello-world-macro/Cargo.toml)
![](examples/macros/hello-world-macro/src/lib.rs)

![](examples/macros/hello-world-use/Cargo.toml)
![](examples/macros/hello-world-use/src/main.rs)


## Macro accepting a single string
{id: macro-accepting-a-single-string}

![](examples/macros/say-hello-macro/src/lib.rs)
![](examples/macros/say-hello-use/out.out)
![](examples/macros/say-hello-use/src/main.rs)


## Accept list of values as a plain string in a macro
{id: accept-list-of-values-as-a-plain-string}

![](examples/macros/say-hello-many-times-macro/Cargo.toml)
![](examples/macros/say-hello-many-times-macro/src/lib.rs)

![](examples/macros/say-hello-many-times-use/Cargo.toml)
![](examples/macros/say-hello-many-times-use/src/main.rs)
![](examples/macros/say-hello-many-times-use/out.out)


## Compile random number in the code using macro
{id: compile-random-number-on-the-code}

![](examples/macros/random-constant-macro/Cargo.toml)
![](examples/macros/random-constant-macro/src/lib.rs)

![](examples/macros/random-constant/Cargo.toml)
![](examples/macros/random-constant/src/main.rs)

TODO: #[macro_export]

## SQLx - compile-time SQL queries
{id: sqlx-compile-time-sql-queries}

TODO
* [SQLx](https://crates.io/crates/sqlx)


## Macro ok! to replace unwrap
{id: macri-ok}

Seen in the tests of the sqlite crate.

```
macro_rules! ok(($result:expr) => ($result.unwrap()));
```

## Error logging
{id: macro-error-logging}

A macro that will replace


```
let x = err_log!(expression);

let x = match expression {
    Ok(val) => val,
    Err(err) => {
        log::error!("{:?}", err),
    }
}
```


