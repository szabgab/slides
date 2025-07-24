# Mocking to reproduce error in our function


* Someone reported that in certain cases the count does not work properly.
* For example when the multi-word name is spread to multiple lines (so there is a newline).
* This is how we can test

{% embed include file="src/examples/mock-lwp/t/webapi_mock_error.t" %}


