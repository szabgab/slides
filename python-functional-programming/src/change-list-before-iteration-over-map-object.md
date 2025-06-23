# Change list before iteration over map object

A small warning. Because **map** only connects to our iterator, but does not iterate over it till it is called,
if we change the content of the underlying iterator, that will be reflected in the results of the iteration over the map object.


{% embed include file="src/examples/functional/change_list_before_map.py" %}
{% embed include file="src/examples/functional/change_list_before_map.out" %}


