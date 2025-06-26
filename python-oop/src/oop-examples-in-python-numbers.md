# OOP in Python (numbers, strings, lists)


There are programming languages such as Java and C# that are Object Oriented languages where in order to do anything, even to print to the screen
you need to understand OOP and implement a class.

Python is Object Oriented in a different way. You can get by without creating your own classes for a very long time in your programming career,
but you are actually using features of the OOP nature of Python from the beginning.

In Python they say "everything is an object" and what they mean is that everything, including literal values such as numbers or strings, or variables holding
a list are instances of some class and that they all the features an instance has. Most importantly they have methods. Methods are just function that are used in
the "object.method()" notation instead of the "function( parameter )" notation.

Some of these methods change the underlying object (e.g. the append method of lists), some will return a copy of the object when the object is immutable. (e.g. the capitalize method of strings).



{% embed include file="src/examples/oop/examples.py" %}




