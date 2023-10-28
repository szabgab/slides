# Variables
{id: variable}

## Variables are immutable
{id: variables-are-immutable}
{i: let}

* Variables in Rust are immutable by default.

![](examples/variables/immutable-number/src/main.rs)
![](examples/variables/immutable-number/out.out)

## Number in a mutable variable
{id: rust-number-in-a-mutable-variable}
{i: let}
{i: mut}

* You can make them mutable by adding the `mut` keyword to the declaration

![](examples/variables/mutable-number/src/main.rs)
![](examples/variables/mutable-number/out.out)

## Literal strings in variables are immutable
{id: literal-strings-in-variables-are-immutable}
{i: let}

* Literal strings and changeable strings are stored differently in Rust.
* Literal strings stored in a variable are immutable.

![](examples/variables/immutable-string/src/main.rs)
![](examples/variables/immutable-string/out.out)

## Literal string in a mutable variable can be replaced
{id: a-literal-string-in-mutable-variable}
{i: let}
{i: mut}

* Use the `mut` keyword to mark a variable as mutable.
* That way we can replace the string...


![](examples/variables/mutable-string/src/main.rs)
![](examples/variables/mutable-string/out.out)

## A literal string cannot be changed
{id: a-literal-string-cannot-be-changed}
{i: push_str}

* ...but we cannot really change it.

![](examples/variables/change-literal-string/src/main.rs)
![](examples/variables/change-literal-string/out.out)

## Really mutable string
{id: really-mutable-string}
{i: String}
{i: from}
{i: push_str}

* We can create a really mutable string using the `String::from` function.

![](examples/variables/really-mutable-string/src/main.rs)
![](examples/variables/really-mutable-string/out.out)

## Cannot change variable type
{id: cannot-change-variable-type}

![](examples/variables/cannot-change-type/src/main.rs)
![](examples/variables/cannot-change-type/out.out)

## Redeclare immutable variable - Shadowing
{id: rust-redeclared-immutable-variable}
{i: let}

* You can actually change even an immutable variable by declaring it again.
* It can be useful if you need to make a few changes and then later no more changes.

![](examples/variables/shadow/src/main.rs)
![](examples/variables/shadow/out.out)

## Redeclare immutable variable and change type - Shadowing
{id: rust-redeclared-immutable-variable-change-type}

* When shadowing we can also change the type of the variable.
* We don't even need to make it mutable.
* e.g. we read from a file or from STDIN a string that we then convert to a number. We can use the same variable name.

![](examples/variables/change-type/src/main.rs)
![](examples/variables/change-type/out.out)


