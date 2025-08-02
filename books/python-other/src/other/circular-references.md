# Circular references

circular references are cleaned up the by the garbage collector
but maybe not all the memory is given back to the OS, and it can take some time to clean them up.

{% embed include file="src/examples/other/circular.py" %}

but weakref might expedite the cleanup. See also the gc module and if I can show it
http://stackoverflow.com/questions/2428301/should-i-worry-about-circular-references-in-python


