# size of map

One advantage of keeping the result of `map` as it is is the memory footprint of the **map object** vs. the generated list.

The `map` function returns a `map` object that takes up a fixed amount of memory, regardless of the size of the original list.

If we flatten it using the `list` function, the size of the generated list will be similar to the size of the original list.

{% embed include file="src/examples/functional/map_size.py" %}

**Output:**

{% embed include file="src/examples/functional/map_size.out" %}
