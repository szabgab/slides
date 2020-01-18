# Testing PHP
{id: testing-php}

## Starting the server
{id: testing-php-starting-server}
{i: php}


In the examples directory start `apache2.pl start`
then you can access the server via http://localhost:8081/php/


## Almost manually testing add()
{id: testing-php-calc}


In the first examples we recreate a path similar to what we
took in the Perl introduction so you might skip it or just
flip through the pages.




Let's assume we have a simple PHP library with a bunch of
functions. It is located in our includes directory in the
mylib.php file. It is used by a "web application" called
basic_calc.php that provides a - surprise - calculator
for the web visitor.




In order to test this we create a separate PHP script that
will require the relevant library and call the add()
function supplying various arguments and displaying the results.




Then we eyeball those results to see if they are what they should be.


![](examples/php/intro/t01.php)


Result:



```
2
4
2
```


Not much of an output but if we are careful we'll see that
the third line is incorrect. The problem is that it is a lot
of effort to check if the results are correct.

dirname(__FILE__) just gives the path to the directory of currently executing file
and we know the library we are testing is relative to it.


## Print expected values as well
{id: testing-php-calc-print-expected}


So the problem is that the test runner has to compute the expected
results every time she runs the test script.

A slight improvement will be to show the expected
results next to the actual values.

![](examples/php/intro/t02.php)


Result:

```
2 == 2
4 == 4
2 == 3
```


This is still hard to follow when there are lots
of cases or even a few cases with large output but it seems to be
a step in the good direction.




## Compare actual with expected values and print only pass/fail
{id: testing-php-calc-compare-with-expected}

![](examples/php/intro/t03.php)

Result:

```
pass
pass
fail
```

Instead of manually comparing the actual results with the expected values
let the computer do the hard work and let it only print if there was a success
or a failure. We introduce some new code that will print "pass" for every case
when the result was the expected value and "fail" when they were different.

This is certainly an improvement but before we further improve our display let's
turn our attention to our own testing code.


## Refactor to get assertTrue
{id: testing-php-calc-compare-with-expected-refactored}

As we are also programmers we will soon recognize that there
is code duplication in our test script and will factor out the
whole printing of pass/fail part to a function that we call assertTrue().
It should receive a true or false value and it will print "pass" or "fail"
accordingly.

![](examples/php/intro/t04.php)

Result:

```
pass
pass
fail
```


As in every refactoring the functionality and the output should remain the
same, just the implementation improves. (Hopefully)




## Introduction to the PHP SimpleTest framework
{id: testing-php-with-simpletest}
{i: simpletest}


That's all very nice but someone has already implemented this with a lot
of other nice features. We are going to look at the SimpleTest framework
of PHP.

[Simpletest](http://www.simpletest.org/)

I am looking at the currently latest 1.0.1 version that already includes autorun.php.

Ubuntu packages the PHP Simpletest package but
`sudo aptitude install php-simpletest`
only gets you version 1.0 which is relatively old.

So the best course of action is to download the simpletest_1.0.1.tar.gz
file from the Simpletest web site and unzip it in a place where your
web server can reach it.


## assertTrue in SimpleTest
{id: testing-php-simpletest-asserttrue}
{i: asssertTrue}

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


![](examples/php/simpletest/st01.php)


Output:


![](examples/php/simpletest/st01.txt)

With the last row being RED



So TestSimple collapses all our individual results and conveniently
only shows the aggregated result and the individual tests that actually failed.

Unfortunately this report only gives us the line number of where the assertion
that failed. No other details about the failure.




## SimpleTest showing success
{id: testing-php-simpletest-on-success}


Just in order so we see it I include an example where I removed
the failing test and in the following example all of the assertions
are successful.


![](examples/php/simpletest/st02.php)


Output:


![](examples/php/simpletest/st02.txt)

With the last row being GREEN




## assertEqual showing the actual values
{id: testing-php-simpletest-assertequal}
{i: asssertEqual}


SimpleTest and its UnitTestCase class provides further methods
for assertions with better error reporting. In the end they
all report assertions but these others have better capabilities
in providing details on the failures.

In our case we could use assertEqual method instead of the assertTrue
method. This one should receive two values. One of them should be the
expected value the other one the actual result. The library does
not make a recommendation which is which, it treats the two values in the
same way and only checks if they are equal or not.


![](examples/php/simpletest/st03.php)


Output:


![](examples/php/simpletest/st03.txt)

With the last row being RED



As you can see there is now a better explanation of what failed.





## SimpleTest showing description of error
{id: testing-php-simpletest-assertequal-description}


The assert* methods of SimpleTest allow an optional additional
parameter which is the description of the current assertion.
In case of failure it will be shown instead of the details of the
error


![](examples/php/simpletest/st04.php)


Output:


![](examples/php/simpletest/st04.txt)

With the last row being RED



## PHP SimpleTest
{id: testing-php-simpletest}


The PHP SimpleTest framework provides lots of additional tools for testing your application.
The documentation for the UnitTestCase class with the list of various assert methods can be found
here:
[unit test documentation](http://simpletest.org/en/unit_test_documentation.html)





## Testing PHP on the command line
{id: testing-php-on-command-line}


Running the test using the web browser will work well during the development
of each test and the relevant code but as the number of tests grow we
will prefer to automate this process and execute it by some automated tool.
Eg. crontab on unix, the scheduler on windows, a smoke testing system
or the post commit hook of your version control system. That will only work if
we can run our tests from the command line.


Luckily SimpleTest and the autorun.php can let us do this.
We can take the last example and run it from the command line:


```
$ php examples/php/simpletest/st04.php
```

The Output is quite similar to what we have in the browser but
this is without any colors.


![](examples/php/simpletest/st04.out)


We can now create a batch file and run all the test files we might have from the
command line. We'll come back to this later.





## Testing PHP Application
{id: testing-php-applications}


While it is nice to know we'll be able to test
each one of the functions or classes on its own in many cases
that's not how things work. For this testing method to work
yo have to be able to separate the functionality of each function
and class and test them in isolation.




Especially when you already have a partially or fully working application
probably written by someone else who wrote spaghetti code, it would
be impossible to write tests in isolation. It will be probably also a waste
of energy as soon you are going to start to clean up that code changing
the internal structure, changing how functions work and building up
- hopefully - a cleaner codebase.




In such cases it is much better to start from the top down. Test the
functionality of the application without even knowing about the internal
structure of the code. Actually the application does not even need to be
written in PHP for this type of testing.




We are going to imitate the web browser, access a web site and check
if the returned page contains the information as we expect.




We subclass the WebTestCase class which provides a `get`
method to retrieve a web page given a URL.

In itself that's not yet an assertion so we wrap it with
the already familiar assertTrue method. We can do that as
WebTestClass is a subclass of UnitTestCase.


![](examples/php/simpletest/web01.php)


The resulting output is similar to what we saw earlier when we
just tried to test an internal function.




## Check web page content
{id: testing-php-check-content}


The previous test only checked if a page was returned but
not the content of the page so we add another assertion
that checks if a given string can be found in the text of the web page.


![](examples/php/simpletest/web02.php)



## Check web page title
{id: testing-php-check-title}


The same way can can check if the page title is correct
using the assertTitle method.


![](examples/php/simpletest/web03.php)



## Check web page content a failure
{id: testing-php-check-content-fails}


It's really nice to see everything working but there will be
times when you encounter a problem. For example that certain text
is missing from the web page:


![](examples/php/simpletest/web04.php)


Will fail with the following output


![](examples/php/simpletest/web04.txt)



## Checking forms
{id: testing-php-check-forms}


To further check if the page is correct we could check,
using assertField(), if the form we expect to be on the
page has the input fields as we expect them. We can even
check if they have the correct preset values.


![](examples/php/simpletest/web05.php)


Unfortunately due to external limitations currently this code
cannot recognize if there are more than one forms on the page
and will mash them together for our purposes.





## Submit form
{id: testing-php-check-submit-form}


The setField can be used to set the value in a field
and the click method to submit submit the form by clicking
a button. After submitting the form we should check if


![](examples/php/simpletest/web06.php)






## Check for text that should not be there.
{id: testing-php-check-for-no-content}


In a previous example we checked if the parts of a form are in
place and then immediately we submitted a form with correct values.




We could in fact check a couple of more things. For example we could check
if the "Result" string appears on the page when we access it for the first time
without parameters.




We could also submit the form with missing or bogus data and see how
the application reacts. Especially we can use the assertNoText assertion
to check if a certain text does NOT appear on the page.


![](examples/php/simpletest/web07.php)


This way we can write test for an application without caring how it was written
or in fact in what languages it is written. Once we are reasonably comfortable
with our tests we can start to refactor the application.







