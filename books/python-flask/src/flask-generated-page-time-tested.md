# Flask generated page - time tested


How can we test the version of our application that also has a generated page? We need to test two pages.

There are many ways to divide our tests.
* We could put all the tests in a single test-function.
* We could have two test-functions in the same test-file.
* We could have two test-functions in two separate test-files.

Putting them in separate functions allows us to run them separately. It also means that if one fails the other might still pass.
Usually we put independent test-cases in separate functions. Because it is still so small, putting them in two separate files seems to be an overkill.

The `test_home` function is relatively straight forward. We get the main page and then we check the status-code and the exact match for the content.

The `test_time` function is trickier. We can't check an exact match as the timestamp will be different every time we run the code. We could **mock**
the time, but we are looking for a simpler solution. So instead of an exact match we use a regexp to check if the result looks like a number we would
expect.

You can run the tests by running `pytest`.

{% embed include file="src/examples/flask/time/test_app.py" %}

```
pytest
```


