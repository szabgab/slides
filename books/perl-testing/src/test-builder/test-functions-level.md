# My own test functions with Test Builder level

* Test::Builder
* $Test::Builder::Level



Behind the scenes both Test::Simple and Test::More use a module
called Test::Builder. Actually Test::Builder is doing the hard work
of counting test and displaying error messages. Test::More is just the
user friendly front end.


Adding the local $Test::Builder::Level = $Test::Builder::Level + 1;
to our own test function will tell Test::Builder to go one level further
back in the call stack to find the location where the function was called
and where the error occurred.

{% embed include file="src/examples/test-perl/t/dice_is_any_fixed.t" %}

Output:

{% embed include file="src/examples/test-perl/t/dice_is_any_fixed.out" %}



