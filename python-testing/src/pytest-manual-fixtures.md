# Manual fixtures (dependency injection)

{% embed include file="src/examples/pytest/test_manual_fixtures.py" %}

**Output:**

{% embed include file="src/examples/pytest/test_manual_fixtures.out" %}

* We can't add fixtures to test_functions as decorators (as I was the case in NoseTest), we need to use dependency injection.


