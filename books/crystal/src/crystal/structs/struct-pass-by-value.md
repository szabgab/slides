# Struct pass-by-value

For immutable structs this is not relevant but when the struct is mutable you have to remember that it is passed by value to functions.
That is, the function receives a copy of the external struct. Any changes made to the struct inside the function will be lost
when you leave the function.

{% embed include file="src/examples/struct/struct_pass_by_value.cr" %}
{% embed include file="src/examples/struct/struct_pass_by_value.out" %}


