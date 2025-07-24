# Testing PHP Application



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


{% embed include file="src/examples/php/simpletest/web01.php" %}


The resulting output is similar to what we saw earlier when we
just tried to test an internal function.




