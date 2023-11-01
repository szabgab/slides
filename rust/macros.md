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

