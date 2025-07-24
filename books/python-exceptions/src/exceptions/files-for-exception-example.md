# File for exception handling example




If we have a list of files and we would like to make sure
we process as many as possible without any problem caused
in the middle, we can catch the exception.



We have the following list of files.
        Notice that "two.txt" is missing and "zero.txt" has a 0 in it.

{% embed include file="src/examples/exceptions/zero.txt" %}
{% embed include file="src/examples/exceptions/one.txt" %}

File two.txt is missing on purpose.

{% embed include file="src/examples/exceptions/three.txt" %}


