# Initialize immutable struct

* initialize

A more realistic example is a struct that has a method called `initialize` that can be used to set the
attributes of the struct. Each variable with a single `@` sign in-front of it is an attribute.

We can initialize some of the attributes by values received from the user and some attributes by generating
the value ourselves. e.g. by using a Time object, a Random value or generating or computing it in any other way.

We can print the content of the Struct, but we have no way to access the attributes and no way to change them.
Hence this struct is immutable.

* There is no way to change this struct
* There is no way to access the individual attributes as there are no getters

{% embed include file="src/examples/struct/initialize_struct.cr" %}
{% embed include file="src/examples/struct/initialize_struct.out" %}


