# Use libraries
{id: use}


## Using the Standard library
{id: using-the-standard-library}
{i: std}
{i: f32}
{i: f64}
{i: consts}
{i: PI}

* [std](https://doc.rust-lang.org/std/)

![](examples/libraries/std-pi/src/main.rs)
![](examples/libraries/std-pi/out.out)

## Using a single value from the Standard library
{id: using-a-single-value-from-the-standard-library}

![](examples/libraries/std-pi-use/src/main.rs)
![](examples/libraries/std-pi-use/out.out)

## Use (import) a name higher up in the hierarchy
{id: use-a-name-higher-up-in-the-hierachy}

There is also an option to include only part of the path in the `use` statement. In this case we will have to use the rest of the path in the code,
but it will allow us to use multiple name (both PI and E in this case) using the shorter name.

![](examples/libraries/std-pi-partial-use/src/main.rs)
![](examples/libraries/std-pi-partial-use/out.out)

## Using a library with an alias
{id: using-library-with-alias}
{i: as}
{i: alias}

If for some reason we really need to use the same name from two different libraries, we can use the `as` keyword to rename one of them
for our project. To give it an alias.

![](examples/libraries/std-pi-use-as/src/main.rs)
![](examples/libraries/std-pi-use-as/out.out)

