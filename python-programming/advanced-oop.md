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


## Monkey patching
{id: monkey-patching-method}

![](examples/classes/person5.py)


## Classes: constructor, instance method
{id: classes}

The "class" keyword creates a "class object". The default constructor of these classes are their own names. So on this case Date() is the constructor.
(The actual code is implemented in the __new__ method of the "object". Calling the constructor will create an "instance object".


Regular functions (methods) defined in a class are "instance methods". They can only be called on "instance objects" and not on the "class object"
as see in the 3rd example.

The attributes created with "self.something = value" belong to the individual instance object.

![](examples/classes/mydate1/mydate.py)
![](examples/classes/mydate1/run.py)

`set_date` is an instance method. We cannot properly call it on a class.

![](examples/classes/mydate1/run.out)

## Class methods and class attributes
{id: class-attributes}
{i: @classmethod}

"total" is an attribute that belongs to the class. We can access it using Date.total. We can create a @classmethod to access it,
but actually we can access it from the outside even without the class method, just using the "class object"


![](examples/classes/mydate3/mydate.py)
![](examples/classes/mydate3/run.py)
![](examples/classes/mydate3/run.out)


## Class methods - alternative constructor
{id: class-methods-alternative-constructor}
{i: @classmethod}

Class methods are used as Factory methods, they are usually good for alternative constructors. In order to be able to use a method as a class-method
(Calling Date.method(...) one needs to mark the method with the @classmethod decorator)

![](examples/classes/mydate2/mydate.py)
![](examples/classes/mydate2/run.py)
![](examples/classes/mydate2/run.out)


## Abstract Base Class
{id: abstract-base-class}

* Create a class object that cannot be used to create an instance object. (It must be subclassed)
* The subclass must implement certain methods required by the base-class.

![](examples/classes/no_abc.py)


## Abstract Base Class with abc
{id: abstract-base-class-with-abc}
{i: abc}

* [abc](https://docs.python.org/library/abc.html)

![](examples/classes/with_abc3.py)
![](examples/classes/with_abc3_real.py)
![](examples/classes/with_abc3_base.py)
![](examples/classes/with_abc3_fake.py)


## Use Python @propery to fix bad interface (the bad interface)
{id: property-fixing-bad-api-original}

When we created the class the first time we wanted to have a field representing the age of
a person. (For simplicity of the example we onlys store the years.)

![](examples/classes/person/person1.py)

Only after releasing it to the public have we noticed the problem. Age changes.

We would have been better off storing birthdate and if necessary calculating the age.

How can we fix this?

## Use Python @propery to fix bad interface (first attempt)
{id: property-fixing-bad-api-first-attempt}

This might have been a good solution, but now we cannot use this as a "fix" as this
would change the public interface from `p.age` to `p.age()`

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
* [property docs](https://docs.python.org/library/functions.html#property)


## Use Python @propery for value validation
{id: property-for-validation}
{i: @property}

![](examples/classes/person/person5.py)
![](examples/classes/person/person5_good.py)
![](examples/classes/person/person5_bad_init.py)
![](examples/classes/person/person5_bad_init.out)
![](examples/classes/person/person5_bad_setter.out)


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

## Destructor delayed
{id: destructor-delayed}

Becasue the object has a reference to itself. (Python uses both reference count and garbage collection.)

![](examples/advanced/destructor_self_reference.py)
![](examples/advanced/destructor_self_reference.out)

## Destructor delayed for both
{id: destructor-sipped}

Because the instances reference each other

![](examples/advanced/destructor_skipped.py)
![](examples/advanced/destructor_skipped.out)


## Opearator overloading
{id: operator-overloading}
{i: __mul__}
{i: __rmul__}

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

## Exercise: Implement a Gene inheritance model combining DNA
{id: exercise-implement-a-gene-inheritance-model}

* A class representing a person. It has an attribute called "genes" which is string of letters. Each character is a gene.
* Implement the `+` operator on genes that will create a new "Person" and for the gene will select one randomly from each parent.

```
a = Person('ABC')
b = Person('DEF')

c = a + b
print(c.gene) # ABF
```

## Exercise: imaginary numbers
{id: exercise-imaginary-numbers}

Create a class that will represent imaginary numbers `(x, y*i)`
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

## Solution: Rectangular
{id: solution-oop-rectangular}

![](examples/advanced/rect/shape2.py)
![](examples/advanced/rect/test_rect.py)


## Solution: Implement a Gene inheritance model combining DNA
{id: solution-implement-a-gene-inheritance-model}

![](examples/advanced/gene_inheritance.py)

