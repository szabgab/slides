# Dancer: Test parameter in route



If you have seen the previous examples then this test script won't surprise you.

The first subtest, called 'main', checks the main page of our web application. Because this is such a small example we check equality here using the **is** function.

The second subtest, called 'one', checks a value that can be a valid user-id.

The third subtest, called 'anything', checks some arbitrary string as a user-id. As you can see, in our current version this call is also expected to work and return the word "anything".
That's right for this test as our current version of the application does not do any input validation.


{% embed include file="src/examples/dancer/params-in-routes/test.t" %}


