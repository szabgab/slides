# Calculator test



How would you make sure this function works correctly?
You'd probably write a small, temporary script to call the function with various
sets of input and you'd then check if the results are as expected.




Let's do that. Write a script using the sum() function of the module and printing the results.


{% embed include file="src/examples/test-simple/tests/t01.pl" %}



In this script we use the $Bin variable of the FindBin module to let perl find the MyTools.pm file.


If you run this script, the output will look like this:

{% embed include file="src/examples/test-simple/tests/t01.pl.out" %}


There was an error on the last line. 2 + 2 + 2 should be 6 and not 4



After some further experimenting we find out that the
problem seems to be, that sum() does not handle more than
2 parameters.

While this is a very simple example, it is easy to overlook the simple
detail, not noticing that one of the results was indeed incorrect.

Of course this is a simple computation and anyone should know
what is the expected result, but what if we are testing something more complex?

Do you know what should be the result? Will you compute it every time
manually to check if that's the correct answer?



We could fix the code, but we will use this case to show how to write tests.

At this point we are not interested in fixing the bug in MyTools.pm.
We are interested in a robust way to write tests for it.

We'll use this example but we have not solved our biggest problems yet:

We cannot expect our test engineers looking at the results to know
the valid result of each line.



