# map on many values

Now imagine you have a very long list. I know this is not such a long list, but I trust you can imagin a long list of numbers. We would like to run
some function on each element and then iterate over the results, but what if at one point in the iteration we decide to `break` out of the loop?

{% embed include file="src/examples/functional/map_with_many_items.py" %}
{% embed include file="src/examples/functional/map_with_many_items.out" %}

You can see that it did not need to waste time calculating the doubles of all the values, as it was calculating on-demand. You can also see that the object returned
from `map` takes up only 56 bytes. Regardless of the size of the original array.



