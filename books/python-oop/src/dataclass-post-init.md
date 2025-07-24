# Dataclasses create init and call post_init


* `__init__` is implemented and that's how the attributes are initialized
* `__post_init__` is called after `__init__` to allow for further initializations

{% embed include file="src/examples/oop/dataclasses_init/shapes.py" %}
{% embed include file="src/examples/oop/dataclasses_init/point.py" %}


