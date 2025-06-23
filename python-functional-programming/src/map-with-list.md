# map with list

map
list

Here too you can use the **list** function to convert all the values at once, but there is an advantage of keeping it as
a **map object**. Not only the size that we already saw with the **range** case, but also the processing time saved by
not calculating the results till you actually need it.


Imagine a case where you apply several expensive (time consuming) transformations to some original list and then you iterate over the end-results
looking for the first value that matches some condition. What if you find the value you were looking for after only a few iteration. Then
making all that expensive calculations to the whole list was a waste of time.

This lazy evaluation can help you save both memory and time and you always have the option to force the immediate calculation by calling the **list**
function.

{% embed include file="src/examples/functional/map_list.py" %}
{% embed include file="src/examples/functional/map_list.out" %}


