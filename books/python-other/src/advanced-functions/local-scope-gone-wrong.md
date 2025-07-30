# Local scope gone wrong

{% embed include file="src/examples/advanced-functions/scoping_external_variable.py" %}
{% embed include file="src/examples/advanced-functions/scoping_external_variable.err" %}


Accessing a global variable inside a function works, but if I change it (make it refer to another piece of data),
then it is disallowed. If I only change the data inside (for mutable variables), that works, but is a bad practice.


