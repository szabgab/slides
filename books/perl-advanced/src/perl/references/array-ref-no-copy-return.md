# Process arrays without copying even the return values

In the previous solution we passed the references to the function
but returned a full array, thereby copying all the values. If we 
care about memory and speed we might eliminate this copying by
returning the reference to the resulting array.

The cost is a small (?) inconvenience as now we have to dereference
the resulting array reference in the calling code.


{% embed include file="src/examples/references/add_arrays_nocopy_return.pl" %}



