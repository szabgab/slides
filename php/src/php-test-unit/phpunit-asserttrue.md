# assertTrue with PHPUnit

In the first example we'll try to solve the same simple problem as we did in the
SimpleTest example. We have a function called add() in the mylib.php file.
We would like to test that function.

We include that file in our test script and include the already installed PHPUnit/Framework.php

We have to create a class that extends PHPUnit_Framework_TestCase - the name of the class does not matter.
In the class we need to create testing functions. The name of each function has to start with 'test',
otherwise the name does not matter. It should be descriptive as any function name.


{% embed include file="src/examples/php/phpunit/calc01.php" %}


As opposed to the SimpleTest framework, in PHPUnit the primary way to execute the tests is from the command line
using the phpunit script. so you do the following:



```
phpunit examples/php/phpunit/cal01.php
```


The output looks like this:


{% embed include file="src/examples/php/phpunit/calc01.php.out)


In the results you can see a single .F meaning one of the testing functions failed.
In addition you'll see details of the failure giving both the name of of the
test function and the test class.



