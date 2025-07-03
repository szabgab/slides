# Refactor larger test suite

Now that we have this tool in place it is time to start to enlarge our test suite.
After all three tests are not enough. As we are adding more and more tests we can
recognize again that there is the data part of the tests that are changing and the
code part which is repeating. This is a good time to refactor our code again.
We take the data and move it to a data structure. The code then can go over this
data structure and execute each unit on its own.


{% embed include file="src/examples/test-simple/tests/t21.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t21.pl.out" %}



For every unit we created an array reference where the last element is the expected
output. Anything before that is the list of parameters.
We then created an array (@tests) of all these units.




In the code we loop over all the units, $t holding the current unit,
and then extract the expected output using pop.
The remaining values are the parameters to the test.
We also generate the name of the test from the input values.




There is a small problem though.
When you add a new test to the array, you also have to remember to update the
tests => 6 line.

There are a number of solution to this problem



