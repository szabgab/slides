# Refactor - Write the ok function


- ok


As we are not only testers but also developers we quickly notice the
repeating pattern and decide to move it to a function so we will write
less code. As we would like to be short, we call the function
**ok()**. As we'll see we are not the only ones who want to
type as little as possible.



This ok() function gets a "true" or "false" value
(that is the result of a comparison such as == in our examples.)



Reminder: In Perl undef, 0, "" and "0" count as false and all other
values as true.


{% embed include file="src/examples/test-simple/tests/t06.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t06.pl.out" %}

But why reinvent the wheel ?


