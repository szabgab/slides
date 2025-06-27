# How can I check if a string can be converted to a number?


* isdecimal
* isnumeric


* This solution only works for integers. Not for floating point numbers.

* We'll talk about this later. For now assume that the user enters something that can be converted to a number.
* Wrap the code in try-except block to catch any exception raised during the conversion.
* Use Regular Expressions (regexes) to verify that the input string looks like a number.
* [Unicode Characters in the 'Number, Decimal Digit' Category](https://www.fileformat.info/info/unicode/category/Nd/list.htm)

* [isdecimal](https://docs.python.org/library/stdtypes.html#str.isdecimal) Decimal numbers (digits) (not floating point)
* [isnumeric](https://docs.python.org/library/stdtypes.html#str.isnumeric) Numeric character in the Unicode set (but not floating point number)
* In your spare time you might want to check out the standard types of Python at [stdtypes](https://docs.python.org/library/stdtypes.html).

{% embed include file="src/examples/basics/isnumber.py" %}

{% embed include file="src/examples/basics/isnumber.out" %}

{% embed include file="src/examples/basics/isnumber2.out" %}

{% embed include file="src/examples/basics/isnumber_other.py" %}

