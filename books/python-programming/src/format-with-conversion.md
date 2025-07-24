# Format with conversion (stringifiation with str or repr)


Adding !s or !r in the place-holder we tell it to cal the str or repr
method of the object, respectively.



* repr (__repr__) Its goal is to be unambiguous
* str (__str__) Its goal is to be readable
* The default implementation of both are useless
* Suggestion
* [Difference between __str__ and __repr__](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

{% embed include file="src/examples/format/format_no_conversion.py" %}
{% embed include file="src/examples/format/format_conversions.py" %}



