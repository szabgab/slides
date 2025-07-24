# JSON dumps


* dumps

* Dictionaries and lists are handles
* Tuples are indistinguishable from lists
* Always Double-quotes
* `null` instead of `None`
* No trailing comma

{% embed include file="src/examples/json/dumps.py" %}
{% embed include file="src/examples/json/dumps.out" %}

`dumps` can be used to take a Python data structure and generate a string in JSON format. That string can then be saved in a file,
inserted in a database, or sent over the wire.


