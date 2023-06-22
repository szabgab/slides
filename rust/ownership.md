# Rust variable ownership
{id: ownership}

## Stack and Heap
{id: stack-and-heap}

* Stack  (fixed size, push/pop)
* Heap   (any size, allocate/free)

## Integers are copies
{id: integers-are-copies}

![](examples/ownership/integers.rs)
![](examples/ownership/integers.out)

## Mutable integers are copies
{id: mutable-integers-are-copies}

![](examples/ownership/mutable_integers.rs)
![](examples/ownership/mutable_integers.out)

## Immutable integers are copies
{id: immutable-integer-are-copies}

![](examples/ownership/immutable_integer.rs)
![](examples/ownership/immutable_integer.out)


## Literal string
{id: literal-string}

* The variable can be made mutable and then it can be replaced, but the literal (hard-coded) string is baked into the code of the program and thus it cannot be changed runtime.
* This is a `&str`

![](examples/ownership/literal_string.rs)

## Mutable string
{id: mutable-string}

* If we declare the variable as a String then the literal value is copied to the heap and it can be changed.

![](examples/ownership/mutable_string.rs)

## Move strings
{id: move-string}

![](examples/ownership/move_string.rs)


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

## Rust ownership string in function
{id: rust-ownership-string-in-function}

![](examples/ownership/string_function.rs)

## Rust ownership borrow string in function
{id: rust-ownership-borrow-string-in-function}
{i: &}

* When passing the variable we need to prefix it with `&`.
* In the function definition we also include the `&` in-front of the type.
* Inside the function we can prefix it with `*` to dereference the variable but in general we don't need to as Rust figures that out.

![](examples/ownership/string_function_borrow.rs)

## Rust function to change string
{id: rust-function-to-change-string}

![](examples/ownership/change_string.rs)

## Rust function to change integer (i32)
{id: rust-function-to-change-integer}

![](examples/ownership/change_i32.rs)

![](examples/ownership/owner.rs)

