# Pytest: Mocking time (test expiration)

In this application the user can "login" by providing their name and then call the `access_page` method within  `session_length` seconds.

Because we know it internally users the `time.time` function to retreive the current time (in seconds since the epoch) we can
replace that function with ours that will fake the time to be in the future.

{% embed include file="src/examples/pytest/time-passed/app.py" %}
{% embed include file="src/examples/pytest/time-passed/test_app.py" %}


