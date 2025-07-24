# Testing GET request with query parameters in Dancer


* GET
* like


Before we go on to the next feature let's make our usual step and write a test for the route handling the query parameters.

The main page now returns a chunk of HTML code. We could repeat the same HTML in our tests, but that would not give as any real value.
We would be better off trying to look for some key elements in the page. In a real-world application that might be verifying if a certain
HTML element is in the response or not. We won't be able to check equality here, so in this example I used the `like` function of Test::More
to compare the content of the page to a regular expression.

The really interesting test is the "echo" subtest where we submit a request with a query string and then check if the result is as we expected.
(The + sign represents a space.)


{% embed include file="src/examples/dancer/get-parameters/test.t" %}

* Run as `prove test.t`



