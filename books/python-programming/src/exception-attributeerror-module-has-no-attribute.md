# Exception: AttributeError: module 'random' has no attribute

* A common mistake. Using the wrong filename.


This works fine:

{% embed include file="src/examples/numbers/my/random.py" %}

This gives an error

{% embed include file="src/examples/numbers/my/rnd.py" %}
{% embed include file="src/examples/numbers/my/rnd.err" %}



Make sure the names of your files are not the same as the names of any of the python packages.


