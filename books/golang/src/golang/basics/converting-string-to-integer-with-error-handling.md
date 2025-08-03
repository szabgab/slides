# Converting string to integer with error handling - strconv, Itoa

* strconv
* Itoa
* nil

* [strconv](https://golang.org/pkg/strconv/)


{% embed include file="src/examples/convert-string-to-integer-error-handling/convert_string_to_integer_error_handling.go" %}
{% embed include file="src/examples/convert-string-to-integer-error-handling/convert_string_to_integer_error_handling.out" %}

This can, of course go wrong. If we ask for an integer and the user types in `"42x"` or even `"FooBar"`. So the conversion might fail. The way Go usually handles errors is by returning a second value which is the special value `nil` if everything went fine, or the error object is something broke. It is the responsibility of the caller to check the error. So in the follwing examples you can see that from each function we accept two values, the actual value we are interested in and another value that we assign to a variable called `err`. It is not a special name, but it is quite common in Go to use the variable name `err` for this purpose.

Then in each one of the example we check if the value of `err` is equal to `nil` or if there was an error in the conversion.

