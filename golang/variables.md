# Variables
{id: variables}

## Variable Declarations
{id: variables-declarations}

* Every variable must be declared.
* Not using a declared variable is a compile-time error.

## Variables - Naming
{id: naming-variables}

* Lower-case variables are scoped to the current package.
* Upper-case variables are exported from the package and globally visible.
* Block-scoped variables (e.g. in a function) are only visible in the block.

* [camelCase](https://en.wikipedia.org/wiki/Camel_case) for private name
* [PascalCase](https://wiki.c2.com/?PascalCase) for public names

* Special case when part of the name is an acronym:
* `theURL`
* `theHTML`


## Declare multiple variables in one line
{id: declare-multiple-variables-in-one-line}

![](examples/declare-multiple-variables/declare_multiple_variables.go)
![](examples/declare-multiple-variables/declare_multiple_variables.out)


## Variables cannot be redefined (no new variables on left side of :=)
{id: no-variable-redeclaration}

![](examples/redefine-variable-fail/redefine_variable_fail.go)
![](examples/redefine-variable-fail/redefine_variable_fail.out)


## At least one new variable on the left side of :=
{id: at-least-one-new-variable-on-the-left-side}

* The existing variable must receive a value of the same type it had earlier.

![](examples/new-variable-on-the-left/new_variable_on_the_left.go)
![](examples/new-variable-on-the-left/new_variable_on_the_left.out)


## Use the same err on the left hand side
{id: redefine-variable}

![](examples/redefine-variable/redefine_variable.go)
![](examples/redefine-variable/redefine_variable.out)


## Package variable
{id: package-variable}

![](examples/package-variables/package_variables.go)
![](examples/package-variables/package_variables.out)


## Shadowing package variable
{id: shadowing-package-variable}

![](examples/shadowing-package-variable/shadowing_package_variable.go)
![](examples/shadowing-package-variable/shadowing_package_variable.out)



## Variable scope
{id: variable-sciope}

![](examples/variable-scope/variable_scope.go)
![](examples/variable-scope/variable_scope.out)

