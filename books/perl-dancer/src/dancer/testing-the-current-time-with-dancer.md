# Testing the current time with Dancer


* like
* qr


Just like in the first case, we would like to make sure our code works now and that it keeps working after we make
changes. So we are going to write a test for this application as well.

However unlike in the previous case, here we cannot compare the results to a fixed value as the result will be
different every time we run the test.

We could mock the time generating code of the Dancer application, but for this application it would be an overkill.

So instead of that we weaken our test and compare the results to a regular expression. So we don't know that the returned
string is indeed the correct date and time, but at least we can know that it looks like one.

The `like` keyword of Test::More provides this testing functionality.


{% embed include file="src/examples/dancer/show_time/test.t" %}

* Run as `prove test.t`



