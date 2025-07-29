# Changing types


Even without any additional work, running mypy on an existing code-base can reveal locations that might need fixing.

For example it can point out places where the content of a variable changes type. Python accepts this, and in some places
this type of flexibility might have advantages, but it can also lead to confusion for the maintainer of this code.


{% embed include file="src/examples/types/simple.py" %}

`python simple.py` works without complaining.

`mypy simple.py` reports the following:

{% embed include file="src/examples/types/simple.out" %}


