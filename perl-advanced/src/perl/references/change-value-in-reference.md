# Change values in a reference

If you create a copy of an array then the two arrays are separated.
Change to any of the arrays is not reflected in the other array.

{% embed include file="src/examples/references/copy_array.pl" %}

When you create a reference to an array, then the referenced array
has the same memory location, hence change in either one of them
is  a change in both of them.

{% embed include file="src/examples/references/change_reference.pl" %}

That means you can pass to a function an array reference,
then from within the function it is easy to change the content of
the original array.


