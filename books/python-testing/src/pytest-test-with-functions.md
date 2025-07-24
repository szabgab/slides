# PyTest: test with functions

If we don't have any of the fixture services we need to write a lot of code:

* We need to call the `setup_db()` in every test.
* We need to call the `teardown_db()` in every test - and it still does not work when the test fails.
* What if there is some work that needs to be done only once and not for every test?

{% embed include file="src/examples/pytest/test_functions.py" %}


**Output:**

{% embed include file="src/examples/pytest/test_functions.out" %}



