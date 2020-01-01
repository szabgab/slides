# Advanced OOP
{id: advanced-oop}

## Class Attributes
{id: attributes}


Class Attributes are inherited by object instances when fetching, but not during assignment.


![](examples/classes/person1.py)


## Attributes with method access
{id: attributes-method-access}


Same as above, but we explicitely set the class attribute during the creation of the class
and we use a method (show) to access it.


![](examples/classes/person2.py)


## Instance Attribute
{id: instance-attribute}


The attributes of the instance object can be set via 'self' from within the class.


![](examples/classes/person3.py)


## Methods are class  attributes
{id: methods-are-class-attributes}


In this example we are going to replace the method in the class by a newly created function.
(monkey patching)


![](examples/classes/person4.py)



## Classes: constructor, instance method
{id: classes}


The "class" keyword creates a "class object". The default constructor of these classes are their own names. So on this case Date() is the constructor.
(The actual code is implemented in the __new__ method of the "object". Calling the constructor will create an "instance object".




Regualar functions (methods) defined in a class are "instance methods". They can only be called on "instance objects" and not on the "class object"
as see in the 3rd example.




The attributes created with "self.something = value" belong to the individual instance object.


![](examples/classes/mydate1/mydate.py)
![](examples/classes/mydate1/run.py)
![](examples/classes/mydate1/run.out)


## Class methods - alternative constructor
{id: class-methods-alternative-constructor}
{i: @classmethod}

Class methods are used as Factory methods, they are usually good for alternative constructors. In order to be able to use a method as a class-method
(Calling Date.method(...) one needs to mark the method with the @classmethod decorator)




Please note, as we can see in the last example, this does not stop you from calling the method on an "instance-object".
In either case the first argument passed will be the "class-object".


![](examples/classes/mydate2/mydate.py)
![](examples/classes/mydate2/run.py)
![](examples/classes/mydate2/run.out)


## Class attributes
{id: class-attributes}


"total" is an attribute that belongs to the class. We can access it using Date.total. We can create a @classmethod to access it,
but actually we can access it from the outside even without the class method, just using the "class object"


![](examples/classes/mydate3/mydate.py)
![](examples/classes/mydate3/run.py)
![](examples/classes/mydate3/run.out)



## Abstract Base Class
{id: abstract-base-class}

* Create a class object that cannot be used to create an instance object. (It must be subclassed)
* The subclass must implement certain methods required by the base-class.

![](examples/classes/no_abc.py)


## Abstract Base Class without abc
{id: abstract-base-class-without-abc}
![](examples/classes/without_abc.py)


## Abstract Base Class with abc
{id: abstract-base-class-with-abc}
{i: abc}
![](examples/classes/with_abc.py)

* [Abstract Base Classes in Python](https://dbader.org/blog/abstract-base-classes-in-python)
* [abc](https://docs.python.org/2/library/abc.html)



## Abstract Base Class with metaclass
{id: abstract-base-class-with-metaclass}
{i: __metaclass__}
![](examples/classes/abc_meta.py)


## Create class with metaclass
{id: create-class-with-metaclass}
![](examples/classes/meta.py)
![](examples/classes/create_class.py)

* [what is a metaclass](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)



## Use Python @propery to fix bad API (the bad API)
{id: property-fixing-bad-api-original}
![](examples/classes/person/person1.py)


## Use Python @propery to fix bad API (first attempt)
{id: property-fixing-bad-api-first-attempt}
![](examples/classes/person/person2.py)


## Use Python @propery to fix bad API
{id: property-fixing-bad-api}
{i: property}

```
property(fget=None, fset=None, fdel=None, doc=None)
```
![](examples/classes/person/person3.py)


## Use Python @propery decorator to fix bad API
{id: property-fixing-bad-api-with-decorators}
{i: @property}
![](examples/classes/person/person4.py)

* [property article](http://www.programiz.com/python-programming/property)
* [property docs](https://docs.python.org/2/library/functions.html#property)



## Use Python @propery for value validation
{id: property-for-validation}
{i: @property}
![](examples/classes/person/person5.py)


## Python Descriptors
{id: descriptors}
{i: __init__}
{i: __get__}
{i: __set__}
{i: __delete__}

A more manual way to implement the property() functionality we have just seen.
Use cases:


* Implement type-checking and/or value checking for attribute setters ()


* [Descriptors](http://intermediatepythonista.com/classes-and-objects-ii-descriptors)
* [Descriptor HowTo Guide](https://docs.python.org/2/howto/descriptor.html)



## class and static methods
{id: static-methods}
{i: @classmethod}
{i: @staticmethod}


Static methods are used when no "class-object" and no "instance-object" is required.
They are called on the class-object, but they don't receive it as a parameter.




They might be better off placed in a module, like the other_method.


![](examples/classes/mydate4/mydate.py)
![](examples/classes/mydate4/run.py)
![](examples/classes/mydate4/run.out)


## Destructor: __del__
{id: destructor}
{i: __init__}
{i: __del__}
![](examples/advanced/destructor.py)
![](examples/advanced/destructor.out)


## Destructor skipped
{id: destructor-sipped}
![](examples/advanced/destructor_skipped.py)
![](examples/advanced/destructor_skipped.out)


## Opearator overloading
{id: operator-overloading}
![](examples/advanced/rect/shapes.py)
![](examples/advanced/rect/rect.py)
![](examples/advanced/rect/rect.out)

In order to make the multiplication work in the other direction, one needs to implement the __rmul__ method.



## Exercise: rectangular
{id: exercise-oop-rectangular}


Take the Rect class in the shapes module. Implement __rmul__, but in that case multiply the width of the rectangular.




Implement the addition of two rectangulars. I think this should be defined only if one of the sides is the same,
but if you have an idea how to add two rectangualars of different sides, then go ahead, implement that.




Also implement all the comparision operators when comparing two rectangulars, compare the area of the two. (like less-than)
Do you need to implement all of them?




## Exercise: SNMP numbers
{id: exercise-snmp-numbers}

* SNMP numbers are strings consisting a series of integers separated by dots: 1.5.2,  3.7.11.2
* Create a class that can hold such an snmp number. Make sure we can compare them with less-than (the comparision is pair-wise for each number until we find two numbers that are different. If one SNMP number is the prefix is the other then the shorter is "smaller").
* Add a class-method, that can tell us how many SNMP numbers have been created.
* Write a separate file to add unit-tests



## Solution: Rectangular
{id: solution-oop-rectangular}
![](examples/advanced/rect/shape2.py)
![](examples/advanced/rect/test_rect.py)


## Exercise: imaginary numbers
{id: exercise-imaginary-numbers}


Create a class that will represent imaginary numbers (x, y*i)
and has methods to add and multiply two imaginary numbers.




```
The math:

z1 = (x1 + y1*i)
z2 = (x2 + y2*i)
z1+z2 = (x1 + x2  + (y1 + y2)*i)

z1*z2 = x1*y1 + x2*y2*i*i + x1*y2*i + x2*y1*i
```


Add operator overloading so we can really write code like:



```
z1 = Z(2, 3)
z2 = Z(4, 7)

zz = z1*z2
```






