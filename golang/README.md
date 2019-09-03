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


## types

* strings are just aliases for byte
* strings are (generally?) immutable

```
s := "some string"
b := []byte(s)    // the ascii or utf values of the characters  ???
```



multiple return values
returning an error from a functions

slide: error handling (functions return the error value)

https://www.callicoder.com/golang-functions/


variadic function
unknown number of parameters?
https://medium.com/rungo/variadic-function-in-go-5d9b23f4c01a


if
https://tour.golang.org/flowcontrol/6
short statement (right before the condition)


variables

how much are they mutable?
do they have methods - nope we only have functions. At least on the basic variables.

converting string to number
(show examples converting "2x"  "" etc) error handling


count digits

for _, digit := range digits {
    count[ digit ]++
}


maps
https://tour.golang.org/moretypes/22


[append to slice](https://tour.golang.org/moretypes/15)
