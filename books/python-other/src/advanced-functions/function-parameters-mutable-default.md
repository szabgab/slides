# Mutable default

The default list assigned to b is created when the f functions is defined.
After that, each call to f() (that does not get a "b" parameter) uses this
common list.


{% embed include file="src/examples/advanced-functions/mutable_default_parameter.py" %}
{% embed include file="src/examples/advanced-functions/mutable_default_parameter.out)

Use None instead:


