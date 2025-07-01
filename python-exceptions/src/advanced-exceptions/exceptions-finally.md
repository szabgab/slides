# Exceptions finally


* finally

* We can add a "finally" section to the end of the "try" - "except" construct.
* The code in this block will be executed after **every** time we enter the **try**.
* When we finish it successfully. When we catch an exception. (In this case a ZeroDivisionError exception in file zero.txt" %}
* Even when we don't catch an exception. Before the exception propagates up in the call stack, we still see the "finally" section executed.

{% embed include file="src/examples/exceptions/finally.py" %}

**Output:**

{% embed include file="src/examples/exceptions/finally.out" %}


