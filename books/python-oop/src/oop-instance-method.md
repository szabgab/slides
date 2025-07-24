# Instance methods


Regular functions (methods) defined in a class are "instance methods". They can only be called on "instance objects" and not on the "class object"
as see in the 3rd example.



The attributes created with "self.something = value" belong to the individual instance object.


{% embed include file="src/examples/oop/mydate1/mydate.py" %}
{% embed include file="src/examples/oop/mydate1/run.py" %}

`set_date` is an instance method. We cannot properly call it on a class.

{% embed include file="src/examples/oop/mydate1/run.out" %}

