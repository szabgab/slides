# Slice

* slice
* len
* cap

* You can view a slice to be just a very flexible array.
* Actually it is a slice of an array. A view on a section of the array.
* len - length
* cal - capacity


The only difference you can see when we create a slice is that we don't explicitely say its size and we also don't put the 3 dots `...` in the square bracket.

There is also a `cap` function that returns the size of the underlying array.

We can access the elements of a slice using the postfix square-bracket notation. Just as with arrays.


{% embed include file="src/examples/slice/slice.go" %}
{% embed include file="src/examples/slice/slice.out" %}


