# map with list

Just as with the `range` object, here with the `map` object too you can use the `list` function to convert all the values at once.

However, there are two advantages of keeping it as a **map object** and not using `list` to flatten it into a `list`.

* Memory usage.
* Delayed (lazy) execution of code.


{% embed include file="src/examples/functional/map_list.py" %}

**Output:**

{% embed include file="src/examples/functional/map_list.out" %}


