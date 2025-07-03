# use BEGIN block with Test::Simple


* BEGIN


Another solution is the use of BEGIN blocks. In case you don't know, code that is placed in a
BEGIN block will be executed as soon as it gets compiled. Even before the rest of the code gets compiled.

So in the next example the array @tests will already have content when perl tries to compile the "use Test::Simple ..."
statement. This way "scalar @tests" will already return the number of elements in the array.

Please note, we have to declare "my @tests" outside the BEGIN block or it will be scoped inside that block.

This is a good solution, though it requires the use of BEGIN, which might be considered as somewhat advanced feature of Perl.


{% embed include file="src/examples/test-simple/tests/t23.pl" %}

Output:

{% embed include file="src/examples/test-simple/tests/t23.pl.out" %}


