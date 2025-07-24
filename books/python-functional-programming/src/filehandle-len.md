# filehandle index and len

On a filehandle (returned by the `open` function) we cannot call the `len` function, nor can we access arbitrary element (row) using index in a square bracket `[]`.
We can only use it as an iterator.

## len

{% embed include file="src/examples/functional/fh_len.py" %}

**Error:**

{% embed include file="src/examples/functional/fh_len.out" %}


## index

{% embed include file="src/examples/functional/fh_index.py" %}

**Error:**

{% embed include file="src/examples/functional/fh_index.out" %}
