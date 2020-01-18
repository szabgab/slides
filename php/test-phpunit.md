# Testing PHP with PHPUnit
{id: test-php-unit}


## Introduction to PHPUnit
{id: phpunit-introduction}


PHPUnit was developed and is maintained by Sebastian Bergmann.
http://sebastian-bergmann.de/
It has an extensive manual and it seems to be more wide-spread than SimpleTest we saw earlier.

The home page is at http://www.phpunit.de/




## assertTrue with PHPUnit
{id: phpunit-asserttrue}


In the first example we'll try to solve the same simple problem as we did in the
SimpleTest example. We have a function called add() in the mylib.php file.
We would like to test that function.

We include that file in our test script and include the already installed PHPUnit/Framework.php

We have to create a class that extends PHPUnit_Framework_TestCase - the name of the class does not matter.
In the class we need to create testing functions. The name of each function has to start with 'test',
otherwise the name does not matter. It should be descriptive as any function name.


![](examples/php/phpunit/calc01.php)


As opposed to the SimpleTest framework, in PHPUnit the primary way to execute the tests is from the command line
using the phpunit script. so you do the following:



```
phpunit examples/php/phpunit/cal01.php
```


The output looks like this:


![](examples/php/phpunit/calc01.php.out)


In the results you can see a single .F meaning one of the testing functions failed.
In addition you'll see details of the failure giving both the name of of the
test function and the test class.




## PHPunit showing success
{id: phpunit-asserttrue-success}


Just in order to see how it looks like I removed the failing test from the test script
and ran the test again.



the code

![](examples/php/phpunit/calc02.php)

Output

![](examples/php/phpunit/calc02.php.out)



## PHPUnit with assertEqual
{id: phpunit-assertequal}


Just as was in the case of the SimpleTest, PHPUnit also has an assertEqual method
that allows the separation of the expected value and the actual result.

The first parameter of the assertEqual method is the expected value and the second
parameter is the actual result. Making the roles of the two values clear is
important so in the reporting we can already know what was the expected and what was the
actual result.


![](examples/php/phpunit/calc03.php)

Output

![](examples/php/phpunit/calc03.php.out)

So the difference between this output and the one from
the first example is that in this case the reader can know more
details about the failure. The reader can actually see that the
expected values was 3 while the actual value was 2. That can
already give a clue where the problem might be.




## assetEqual with message
{id: phpunit-assertequal-message}


assertEqual can actually get a third parameter too.
This can hold a short description of what is being tested.


![](examples/php/phpunit/calc04.php)

Output



In case of success this does not make a difference but when the
test fails PHPUnit will display this message along with the
name of the test function and the name of the test class.
If the message is worded carefully it can further help in
understanding the failure without even looking at the source code.


![](examples/php/phpunit/calc04.php.out)




## Installing PHP Unit
{id: phpunit-installing}


You should be able to install PHPUnit either by the package management system
of your operating system or via PEAR. http://pear.php.net/

In Ubuntu 9.04 I found I could install it using

sudo aptitude install phpunit

but that seems to bring a very old version of PHPUnit.




In order to use PEAR first I had to install the command line tool using

sudo aptitude install php-pear

Then I followed the instructions on the PHPUnit web site
though I had to use sudo for that as it would not work as regular user.

sudo channel-discover pear.phpunit.de

gave me the following error message:

$ sudo pear install phpunit/PHPUnit
Did not download optional dependencies: pear/Image_GraphViz, pear/Log, use --alldeps to download automatically
phpunit/PHPUnit requires PEAR Installer (version >= 1.8.1), installed version is 1.7.1
phpunit/PHPUnit can optionally use package "pear/Image_GraphViz" (version >= 1.2.1)
phpunit/PHPUnit can optionally use package "pear/Log"
phpunit/PHPUnit can optionally use PHP extension "pdo_sqlite"
phpunit/PHPUnit can optionally use PHP extension "xdebug" (version >= 2.0.0)
No valid packages found
install failed

So I had to first upgrade PEAR which was easy:

$ sudo pear upgrade-all

and then I could install PHPUnit:

$ sudo pear install phpunit/PHPUnit


It might be slightly different on your operating system.








