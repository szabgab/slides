# Use libraries
{id: use}


## Using the Standard library
{id: using-the-standard-library}

* [std](https://doc.rust-lang.org/std/)

![](examples/intro/std_pi.rs)
![](examples/intro/std_pi.out)

## Using a single value from the Standard library
{id: using-a-single-value-from-the-standard-library}

![](examples/intro/std_pi_use.rs)
![](examples/intro/std_pi_use.out)

## Use (import) a name higher up in the hierarchy
{id: use-a-name-higher-up-in-the-hierachy}

There is also an option to include only part of the path in the `use` statement. In this case we will have to use the rest of the path in the code,
but it will allow us to use multiple name (both PI and E in this case) using the shorter name.

![](examples/intro/std_pi_partial_use.rs)
![](examples/intro/std_pi_partial_use.out)

## Using a library with an alias
{id: using-library-with-alias}
{i: as}
{i: alias}

If for some reason we really need to use the same name from two different libraries, we can use the `as` keyword to rename one of them
for our project. To give it an alias.

![](examples/intro/std_pi_use_as.rs)
![](examples/intro/std_pi_use_as.out)
