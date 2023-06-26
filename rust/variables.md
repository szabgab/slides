# Variables
{id: variable}

## Variables are immutable
{id: variables-are-immutable}
{i: let}

* Variables in Rust are immutable by default.

![](examples/variables/number_immutable.rs)
![](examples/variables/number_immutable.out)

## Number in a mutable variables
{id: rust-number-in-mutable-variables}
{i: let}
{i: mut}

![](examples/variables/number_mutable.rs)
![](examples/variables/number_mutable.out)

## Variables are immutable by default
{id: immutable-literal-string}
{i: let}

* Variables are immutable by default

![](examples/variables/immutable_string.rs)
![](examples/variables/immutable_string.out)

## String in a mutable variable
{id: a-literal-string-in-mutable-variable}
{i: let}
{i: mut}

* Use the `mut` keyword to mark a variable as mutable.

![](examples/variables/mutable_string.rs)
![](examples/variables/mutable_string.out)

## Redeclare immutable variable - Shadowing
{id: rust-redeclared-immutable-variable}
{i: let}

* You can actually change even an immutable variable by declaring it again.
* It can be useful if you need to make a few changes and then later no more changes.

![](examples/variables/shadow.rs)
![](examples/variables/shadow.out)

## Redeclare immutable variable and change type - Shadowing
{id: rust-redeclared-immutable-variable-change-type}

* When shadowing we can also change the type of the variable.
* e.g. we read from a file or from STDIN a string that we then convert to a number. We can use the same variable name.

![](examples/variables/change_type.rs)
![](examples/variables/change_type.out)


