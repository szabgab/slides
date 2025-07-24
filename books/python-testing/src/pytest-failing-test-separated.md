# Pytest failing test separated

Instead of putting the two asserts in the same test function we could also put them in separate onese like in this example.

{% embed include file="src/examples/pytest/math/test_mymath_more_separate.py" %}

The result of running this test file shows that it `collected 2 items` as there were two test functions.

Then next to the test file we see a dot indicating the successful test case and an F indicating the failed test. The more detailed test report helps.

At the bottom of the report you can also see that now it indicates 1 failed and 1 passed test.

{% embed include file="src/examples/pytest/math/test_mymath_more_separate.out" %}

