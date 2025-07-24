# map

* map


`map` will transform the content of a list.


Given a list of values that can come from an array or from calling the `keys` function on a hash or in any other way, we can apply a transformation
on each element and then collect the transformed values on the left hand side of the assignment. e.g. in an array.

On each iteration the current element is placed in the `$_` variable, the code in the block is executed, and the result is passed to the left-hand-side
that collects all the responses.


```
ARRAY = map BLOCK LIST
```
{% embed include file="src/examples/functional/map_perl.pl" %}


