# Slice Pointer and copy slice

* copy

* Assigning a slices assigns the reference to the slice, to the same place in memory.
* However if we then change one of the variables (e.g. enlarge it), it might be moved to another array and then the two get separated.
* If we assign a pointer to the slices, that pointer goes to the "head of the slice" which is moved when we move the slice.

{% embed include file="src/examples/slice-pointer/slice_pointer.go" %}
{% embed include file="src/examples/slice-pointer/slice_pointer.out" %}

