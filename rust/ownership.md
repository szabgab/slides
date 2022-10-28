# Rust variable ownership
{id: ownership}

## Rust ownership str
{id: rust-ownership-str}

![](examples/ownership/str.rs)

## Rust ownership String
{id: rust-ownership-string}


* A variable owns a string.
* If we assign it to another variable the ownership passes to that variable.
* The old owner cannot use it now.

![](examples/ownership/string.rs)

## Rust clone a String
{id: rust-ownership-clone-string}
{i: clone}

* In some cases what we will want is to copy the content of the variable.
* For this we can use the `clone` method.

![](examples/ownership/string_clone.rs)

## Rust ownership - borrow String
{id: rust-ownership-borrow-string}
{i: &}

* We can tell Rust that a variable borrows the ownership.
* In this case both variables have (read) access to the variable.
* We can have as many (read) borrows as we need.

![](examples/ownership/string_borrow.rs)

## Rust ownership
{id: rust-ownership-string-in-function}

![](examples/ownership/string_function.rs)

![](examples/ownership/string_function_borrow.rs)

