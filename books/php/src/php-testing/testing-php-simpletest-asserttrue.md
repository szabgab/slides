# assertTrue in SimpleTest

* asssertTrue

So we unzipped the simpletest zip file to a directory in the course
directory structure some 3 levels above the actual examples.




The first thing we'll have to do in our code is to load the
autorun.php file from the simpletest directory. That file, as its
name also reveals will run our tests automatically when we hit the
page.




The next thing is to pay the overhead of the test writing. Luckily we'll
only need to pay it once for every group of tests. This is Object Oriented
code but even if you are not yet familiar with OO you don't have to worry.
The tests themselves are simple functions calls.

We need to create a class that extends UnitTestCase class provided by SimpleTest.
The name ( in our example TestOfAdd ) of the class does not really matter but as usual,
it is better if it is descriptive of what the tests are going to, err ... test.

Withing the class we need to implement a function ( testAdd in our example ) that
will include the test cases. In the case of the function the name has to start with "test"
but beyond that it does not matter what exactly it is. It should be descriptive.

Within the function we can call the assertTrue method on the $this object. For those
not familiar with OO, $this is provided automatically and the -> notion is just
a fancy way of calling the assertTrue() function.


{% embed include file="src/examples/php/simpletest/st01.php" %}


Output:


{% embed include file="src/examples/php/simpletest/st01.txt)

With the last row being RED



So TestSimple collapses all our individual results and conveniently
only shows the aggregated result and the individual tests that actually failed.

Unfortunately this report only gives us the line number of where the assertion
that failed. No other details about the failure.



