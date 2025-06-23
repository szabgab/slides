# Get indices of values

`filter` can help us get a sublist of values from an iterable, eg. from a list that match some condition.
In this example we see how to get all the names that are exactly 3 characters long.

What if, however if instead of the values themselves, you would like to know their location? The indexes of the
places where these value can be found. In that case, you would run the `filter` on the indexes from 0 till the last
valid index of the list. You can do that using the `range` function.

Finally there is another example that shows how to get the indexes of all the names that have an "e" in them.
Just to show you that we can use any arbitray condition there.

{% embed include file="src/examples/functional/get_indexes.py" %}
{% embed include file="src/examples/functional/get_indexes.out" %}



