# Read all the characters into a string (slurp)

* read


In some other cases, especially if you are looknig for some pattern that starts on one line but ends on another line.
you'd be better off having the whole file as a single string in a variable. This is where the `read` method comes in handy.

It can also be used to read in chunks of the file.


{% embed include file="src/examples/files/slurp.py" %}

**Output:**

{% embed include file="src/examples/files/slurp.out" %}



read(20) will read 20 bytes.



