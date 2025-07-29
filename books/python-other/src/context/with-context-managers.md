# Context managers with class

* __enter__
* __exit__


Even if there was en exception in the middle of the process,
the __exit__ methods of each object will be called.

{% embed include file="src/examples/context/context-managers.py" %}
{% embed include file="src/examples/context/context-managers.out" %}



