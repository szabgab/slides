# Access map element (that does not exist)

* What happens when we access an element that does not exist?
* Go returns 0.
* So we can't know if the field exists and its value is 0 or if it does not exist at all.

{% embed include file="src/examples/access-map-element/access_map_element.go" %}
{% embed include file="src/examples/access-map-element/access_map_element.out" %}


