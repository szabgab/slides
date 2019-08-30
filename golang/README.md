fmt.Printf("%#v", expr)
or implement the String method of the class to be able to use %s


## variables

Not using a declared variable is a compile-time error!


* Redeclaration and shadowing
* Visibility
* Naming conventions
* Type conversions

* lower-case variables are scoped to the current package
* upper-case variables are exported from the package and globally visible
* block-scoped variables (e.g. in a function) are only visible in the block

* theURL
* theHTML
