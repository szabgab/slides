# Question mark: ?

* ?

* meaning "or nil" in type definitions `String?` is the same as `String | Nil`
* Methods ending with `?` usually return a boolean (true, false) - there is no enforcement of this in Crystal
* If a construct might raise an exception adding a question mark can convert that into returning nil
* It is also part of the conditional operator `?:`

{% embed include file="src/examples/other/questionmark.cr" %}


