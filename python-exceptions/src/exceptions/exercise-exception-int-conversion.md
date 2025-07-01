# Exercise: Exception int conversion


* In the earlier example we learned how to handle both ZeroDivisionError and FileNotFoundError exceptions. Now try this


```
cd examples/exceptions
python handle_both_exceptions.py one.txt zero.txt two.txt text.txt three.txt
```
{% embed include file="src/examples/exceptions/handle_both_exceptions.out" %}

* This will raise a `ValueError` exception before handling file three.txt
* Fix it by capturing the specific exception.
* Fix by capturing "all other exceptions".

{% embed include file="src/examples/exceptions/text.txt" %}


