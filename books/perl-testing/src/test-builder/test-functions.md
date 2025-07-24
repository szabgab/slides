# My own test functions

After writing lots of tests, you'll see that you need the above code (with the extra diag)
in several places in your tests script, so you'll want to refactor it
and create a function wrapping it.

The story behind is that the dice() function can actually get any number ($n) and it
should then produce a random whole number between 1 and $n. The default is 6. So we
are testing dice() with several possible parameters.

{% embed include file="src/examples/test-perl/t/dice_is_any.t" %}



We move the ok() to a function call is_any and we are calling it with the actual value,
a reference to an array holding the expected values and the name of the test uint.
We had to slightly change the part of the ok() as now we have a reference to the expected
values and not the array itself.


Output:

{% embed include file="src/examples/test-perl/t/dice_is_any.out" %}



This seems to be ok but we have a slight problem here. The row number displayed in the
error report is the row number where we actually call the ok() and not where we call the
is_any().



