# Slice of an array

* len
* cap


We can use the `array[start:end]` syntax to get a slice of the array. The returned object is called a `slice` and it is a window onto the underlying array.
It has a length defined by the `start` and `end` of the slice. It also has a capacity, which is all the places in the array from the `start` of the sliced to the end of the array.


{% embed include file="src/examples/slice-of-array/slice_of_array.go" %}
{% embed include file="src/examples/slice-of-array/slice_of_array.out" %}


