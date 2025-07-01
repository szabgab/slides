# How to raise an exception


* raise
* throw
* Exception


As you create more and more complex applications you'll reach a point where you write a function, probably in a module, that needs to report some error condition.
You can raise an exception in a simple way.


{% embed include file="src/examples/exceptions/raise.py" %}

```
$ python raise.py 
Adding apple: 3
Exception: Amount of sugar must be positive. -1 was given.
Type: Exception
Adding banana: 2
```


