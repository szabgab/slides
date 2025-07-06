# assertEqual showing the actual values

* asssertEqual


SimpleTest and its UnitTestCase class provides further methods
for assertions with better error reporting. In the end they
all report assertions but these others have better capabilities
in providing details on the failures.

In our case we could use assertEqual method instead of the assertTrue
method. This one should receive two values. One of them should be the
expected value the other one the actual result. The library does
not make a recommendation which is which, it treats the two values in the
same way and only checks if they are equal or not.


{% embed include file="src/examples/php/simpletest/st03.php" %}


Output:


{% embed include file="src/examples/php/simpletest/st03.txt)

With the last row being RED



As you can see there is now a better explanation of what failed.

