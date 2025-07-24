# Type checking

* int
* String



We can declare the types of variables, but that does not make any difference during normal run-time.
We can still assign values of other types to the variable, and it sill only recognizes
real type-mismatch in use at run-time.

{% embed include file="src/examples/dart-intro/type_checking.dart" %}

**dart type_checking.dart** (production mode)



 will throw exception on `c+d`.


{% embed include file="src/examples/dart-intro/type_checking.out)

**dart --checked type_checking.dart** (checked mode)



 will throw exception already on `b = 'abc';`.


{% embed include file="src/examples/dart-intro/type_checking_checked.out)

IDE




The IDE will put little warning marks both of the above lines, and if we run it in the IDE we'll get an error
at the same line where the --checked version go the exception.


```
Breaking on exception: type 'String' is not a subtype of type 'int' of 'b'.
```

Dart is an optionally typed and dynamic language. Variables can be


* annotated with static types
* untyped (aka. dynamic)


