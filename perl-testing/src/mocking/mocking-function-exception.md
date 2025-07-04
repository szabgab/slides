# Mocking exception


* What if the `get` function raises an exception, how will our code handle?
* Hint: it does not, so this test will break
* But this is how we could test what will happen in that case without trying to figure out how to reliably create one using the real LWP::Simple

{% embed include file="src/examples/mock-lwp/t/webapi_mock_exception.t" %}


