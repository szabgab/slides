# Handling errors as return values


* Each function that fails returns some error indicator. `None` ? An object that has and attribute "error"?
* `None` would be bad as that cannot indicate different errors.
* Every called needs to check if the function returned error. If at any point we forget our system might run with hidden failures.


{% embed include file="src/examples/exceptions/demo1.py" %}

* If we forget to check the result and pass it on, we might get some error in the code that is quite far from where the error actually happened

{% embed include file="src/examples/exceptions/demo2.py" %}

* This can happen even if we don't pass the result around:

{% embed include file="src/examples/exceptions/demo3.py" %}



