# Several defaults, using names

* non-keyword arg after keyword arg


Parameters with defaults must come at the end of the parameter declaration.


{% embed include file="src/examples/functions/named_params_and_defaults.py" %}

{% embed include file="src/examples/functions/named_and_positional_bad.py" %}

**Output:**

{% embed include file="src/examples/functions/named_and_positional_bad.out" %}


There can be several parameters with default values.
They are all optional and can be given in any order after the positional arguments.


