# Changing types when reading a number


A quite common case in the real-world when you read in something that is supposed to be a number.
In terms of the Python type-system the input is always a string. Even if it looks like a number.
We then need to convert it to int() or to float() to use them as such.

People will often reuse the same variable to first hold the string and then the number. This is ok with Python,
but might be confusingt to the reader.


{% embed include file="src/examples/types/input.py" %}

`mypy input.py` will print the following:

{% embed include file="src/examples/types/input.out" %}


