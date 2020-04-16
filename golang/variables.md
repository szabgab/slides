# Variables
{id: variables}

## Variables intro
{id: variables-intro}

* Every variable must be declared.
* Not using a declared variable is a compile-time error.

## Variables - Naming
{id: naming-variables}

* Lower-case variables are scoped to the current package.
* Upper-case variables are exported from the package and globally visible.
* Block-scoped variables (e.g. in a function) are only visible in the block.

* theURL
* theHTML

* [camelCase](https://en.wikipedia.org/wiki/Camel_case) for private name
* [PascalCase](https://wiki.c2.com/?PascalCase) for public names

## Declare multiple variables in one line
{id: declare-multiple-variables-in-one-line}

![](examples/declare-multiple-variables/declare_multiple_variables.go)
![](examples/declare-multiple-variables/declare_multiple_variables.out)


## No Variable Redeclaration
{id: no-variable-redeclaration}

![](examples/redefine-variable-fail/redefine_variable_fail.go)
![](examples/redefine-variable-fail/redefine_variable_fail.out)


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

