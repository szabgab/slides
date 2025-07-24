# range index and len

Similar to strings, lists, and tuple, but unlike filehandles, we can use the `len` function on the `range` object and we can also access a specific element
using the square-bracket indexing without actually iterating over all the elements.


{% embed include file="src/examples/functional/range_len.py" %}

**Output:**

{% embed include file="src/examples/functional/range_len.out" %}
