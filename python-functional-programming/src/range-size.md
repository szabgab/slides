# range vs. list size


Showing that the range object remains the same size regardless of the size of the range, but if we convert it into a list then its
memory footprint is proportional to its size. To the number of elements in it.

In this example we have a loop iterating over **range(21)**, but that's only for the convenience, the interesting part is inside the loop.
On every iteration call **range()** with the current number, then we convert the resulting object into a list of numbert. Finally we print out
the current number and the size of both the object returned by **range()** and the list generated from the object. As you can see the memory usage
of the **range** object remains the same 48 byttes, while the memory usage of the list growth as the list gets longer.


{% embed include file="src/examples/functional/range_size.py" %}

**Output:**

{% embed include file="src/examples/functional/range_size.out" %}

* getsizeof

