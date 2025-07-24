# Alternative constructor with class method


* @classmethod


Class methods are used as Factory methods, they are usually good for alternative constructors. In order to be able to use a method as a class-method
(Calling Date.method(...) one needs to mark the method with the `@classmethod` decorator)


* Normally we create a Date instance by passing 3 numbers for Year, Monh, Day.
* We would also like to be able to create an instance using a string like this: `2021-04-07`

{% embed include file="src/examples/oop/mydate2/mydate.py" %}
{% embed include file="src/examples/oop/mydate2/run.py" %}
{% embed include file="src/examples/oop/mydate2/run.out" %}

