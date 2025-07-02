# Test POST requests in Dancer



Testing a POST request is as simple as testing a GET request.

In the test if the index page we need to expect the method="POST".

In the echo subtest we use the POST keyword to tell the client to send in a POST-request and we pass in the content of
the body as an anonymous hash.


{% embed include file="src/examples/dancer/post-parameters/test.t" %}

* Run as `prove test.t`


