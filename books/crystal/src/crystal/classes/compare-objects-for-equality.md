# Compare objects for equality

Normally using `==` between two instances will only return `true` if they are the exact same objects in the memory.
If "only" all the attributes are the same then `==` will be `false`.

To be able to compare two objects based on their attributes only we can used the `def_equals` macro.

* [Object](https://crystal-lang.org/api/Object.html)

{% embed include file="src/examples/classes/compare_objects.cr" %}


