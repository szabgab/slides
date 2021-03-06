# Advanced OOP
{id: advanced-oop}

## Stringify class
{id: class-stringification}
{i: __str__}
{i: __repr__}

* __repr__ "should" return Python-like code
* __str__ should return readable representation
* If __str__ does not exist, __repr__ is called instead.

![](examples/oop/stringification/shapes.py)
![](examples/oop/stringification/run.py)



## Multiple inheritance
{id: oop-multiple-inheritance}

![](examples/oop/inheritance/multi.py)
![](examples/oop/inheritance/multi.out)

* [mro - method resolution order](https://www.python.org/download/releases/2.3/mro/)

## Multiple inheritance - diamond
{id: oop-multiple-inheritance-diamond}

* Not Bot ParentA and ParentB inherit attributes from GrandParent,
* but they are now merged.

![](examples/oop/inheritance/diamond.py)

## Interfaces
{id: oop-interfaces}

* Parent and Child can have attributes
* Tools only has methods

![](examples/oop/inheritance/interface.py)
![](examples/oop/inheritance/interface.out)

## Abstract Base Class
{id: oop-abstract-base-class}

* Create a class object that cannot be used to create an instance object. (It must be subclassed)
* The subclass must implement certain methods required by the base-class.

## Abstract Base Class with abc
{id: oop-abstract-base-class-with-abc}
{i: abc}
{i: abstractmethod}

* [abc](https://docs.python.org/library/abc.html)

![](examples/oop/abc/with_abc3.py)

## ABC working example
{id: oop-abc-working-example}

![](examples/oop/abc/with_abc3_real.py)
![](examples/oop/abc/with_abc3_real.out)

## ABC - cannot instantiate the base-class
{id: oop-abc-no-instance-from-base-class}

![](examples/oop/abc/with_abc3_base.py)
![](examples/oop/abc/with_abc3_base.out)

## ABC - must implement methods
{id: oop-abc-must-implement-methods}

![](examples/oop/abc/with_abc3_fake.py)
![](examples/oop/abc/with_abc3_fake.out)

## Class Attributes
{id: oop-class-attributes}

* Class attributes can be created inside a class.
* Assign to class attribute and fetch from it.
* Class attributes can be also created from the outside.
* Creating a instance does not impact the class attribute.

![](examples/oop/person1.py)

## Class count instances
{id: oop-class-count-instances}

![](examples/oop/counter_increase.py)

## Destructor: __del__
{id: destructor}
{i: __init__}
{i: __del__}

![](examples/oop/destructor.py)
![](examples/oop/destructor.out)


## Class count instances - decrease also (destructor: __del__)
{id: oop-class-count-instances-decrease-also}
{i: __del__}

![](examples/oop/counter_decrease.py)

## Keep track of instances
{id: oop-keep-track-of-instances}

![](examples/oop/keep_track.py)
![](examples/oop/keep_track.out)


## Keep track of instances properly (weakref)
{id: oop-keep-track-of-instances-properly}
{i: weakref}

![](examples/oop/keep_track_properly.py)
![](examples/oop/keep_track_properly.out)

## Destructor delayed
{id: oop-destructor-delayed}

Because the object has a reference to itself. (Python uses both reference count and garbage collection.)

![](examples/oop/destructor_self_reference.py)
![](examples/oop/destructor_self_reference.out)

## Destructor delayed for both
{id: oop-destructor-delayed-for-both}

Because the instances reference each other

![](examples/oop/destructor_both.py)
![](examples/oop/destructor_both.out)


## Class Attributes in Instances
{id: oop-class-attributes-in-instances}

![](examples/oop/person11.py)


## Attributes with method access
{id: oop-attributes-method-access}

* Use a method (show) to access it.

![](examples/oop/person2.py)

## Methods are class attributes - add method
{id: oop-methods-are-class-attributes}

{aside}
In this example we are going to add a newly created method to the class.
(monkey patching)
{/aside}

![](examples/oop/add_method.py)

## Methods are class attributes - replace method
{id: oop-methods-are-class-attributes-replace-method}

{aside}
In this example we are going to replace the method in the class by a newly created function.
(monkey patching)
{/aside}

![](examples/oop/replace_method.py)


## Methods are class attributes - Enhance method (Monkey patching)
{id: oop-enhance-method-monkey-patching}

![](examples/oop/enhance/shapes.py)
![](examples/oop/enhance/enhance_method.py)
![](examples/oop/enhance/enhance_method.out)
![](examples/oop/enhance/tools.py)


## Method types
{id: oop-method-types}

* Instance methods - working on self
* Class methods - working on the class (e.g. alternative constructor)
* Static methods - have no self or class (helper functions)

## Instance methods
{id: oop-instance-method}

{aside}
Regular functions (methods) defined in a class are "instance methods". They can only be called on "instance objects" and not on the "class object"
as see in the 3rd example.
{/aside}

{aside}
The attributes created with "self.something = value" belong to the individual instance object.
{/aside}

![](examples/oop/mydate1/mydate.py)
![](examples/oop/mydate1/run.py)

`set_date` is an instance method. We cannot properly call it on a class.

![](examples/oop/mydate1/run.out)

## Class methods
{id: oop-class-methods}
{i: @classmethod}

* Access class attributes
* Create alternative constructor

## Class methods accessing class attributes
{id: oop-class-methods-accessing-class-attributes}
{i: @classmethod}

{aside}
"total" is an attribute that belongs to the class. We can access it using Date.total. We can create a `@classmethod` to access it,
but actually we can access it from the outside even without the class method, just using the "class object"
{/aside}

![](examples/oop/mydate3/mydate.py)
![](examples/oop/mydate3/run.py)
![](examples/oop/mydate3/run.out)


## Default Constructor
{id: oop-default-constructor}

* The "class" keyword creates a "class object". The default constructor of these classes are their own names.
* The actual code is implemented in the `__new__` method of the `object`.
* Calling the constructor will create an "instance object".


## Alternative constructor with class method
{id: oop-class-methods-alternative-constructor}
{i: @classmethod}

{aside}
Class methods are used as Factory methods, they are usually good for alternative constructors. In order to be able to use a method as a class-method
(Calling Date.method(...) one needs to mark the method with the `@classmethod` decorator)
{/aside}

* Normally we create a Date instance by passing 3 numbers for Year, Monh, Day.
* We would also like to be able to create an instance using a string like this: `2021-04-07`

![](examples/oop/mydate2/mydate.py)
![](examples/oop/mydate2/run.py)
![](examples/oop/mydate2/run.out)

## Static methods
{id: oop-static-methods}
{i: @staticmethod}

{aside}
Static methods are used when no "class-object" and no "instance-object" is required.
They are called on the class-object, but they don't receive it as a parameter.
{/aside}

![](examples/oop/static_method/mydate.py)
![](examples/oop/static_method/run.py)
![](examples/oop/static_method/run.out)

## Module functions
{id: oop-module-functions}

{aside}
Static methods might be better off placed in a module as simple functions.
{/aside}

![](examples/oop/module_function/mydate.py)
![](examples/oop/module_function/run.py)
![](examples/oop/module_function/run.out)


## Class and static methods
{id: oop-class-and-static-methods}
{i: @classmethod}
{i: @staticmethod}


![](examples/oop/class_and_static_method/mydate.py)
![](examples/oop/class_and_static_method/run.py)
![](examples/oop/class_and_static_method/run.out)


## Special methods
{id: special-class-methods}
{i: __str__}
{i: __repr__}

* `__str__`
* `__repr__`
* `__eq__`
* `__lt__`
* ...


## Opearator overloading
{id: oop-operator-overloading}
{i: __mul__}
{i: __rmul__}

![](examples/oop/rect/shapes.py)
![](examples/oop/rect/rect.py)
![](examples/oop/rect/rect.out)

In order to make the multiplication work in the other direction, one needs to implement the __rmul__ method.

## Operator overloading methods
{id: oop-operator-overloading-methods}
{i: __mul__}
{i: __rmul__}
{i: __add__}
{i: __radd__}
{i: __iadd__}
{i: __lt__}
{i: __le__}

```
*    __mul__,  __rmul__
+    __add__, __radd__
+=   __iadd__
<    __lt__
<=   __le__
...
```

* [see all of them in datamodel](https://docs.python.org/reference/datamodel.html)

## Declaring attributes (dataclasses)
{id: dataclass}

* Starting from 3.7 [dataclasses](https://docs.python.org/library/dataclasses.html)
* Typehints are required but not enforced!

![](examples/oop/dataclasses/shapes.py)
![](examples/oop/dataclasses/point.py)

## Dataclasses and __repr__
{id: dataclass-and-repr}

* `__repr__` is implemented

![](examples/oop/dataclasses/repr.py)

## Dataclasses and __eq__
{id: dataclass-provide-eq}

* `__eq__` is automatically implemented

![](examples/oop/dataclasses/compare.py)

__eq__ are automatically implemented

## Dataclasses create __init__ and call __post_init__
{id: dataclass-post-init}

* `__init__` is implemented and that's how the attributes are initialized
* `__post_init__` is called after `__init__` to allow for further initializations

![](examples/oop/dataclasses_init/shapes.py)
![](examples/oop/dataclasses_init/point.py)

## Dataclasses can provide default values to attributes
{id: dataclasses-default}

![](examples/oop/dataclasses_default/shapes.py)
![](examples/oop/dataclasses_default/point.py)

* Attributes with default values must before attributes without default

## Dataclasses and default factory
{id: dataclasses-and-default-factory}

![](examples/oop/dataclasses_default/fruits.py)

## Read only (frozen) Dataclass
{id: read-only-dataclass}

* `@dataclass(frozen = True)`    makes the class immutable

![](examples/oop/dataclasses_frozen/shapes.py)
![](examples/oop/dataclasses_frozen/point.py)



## Serialization of instances with pickle
{id: selialization-with-pickle}
{i: pickle}

![](examples/classes/serialization_with_pickle.py)

## Class in function
{id: class-in-function}

![](examples/oop/class_in_function.py)


## Exercise: rectangle
{id: exercise-oop-rectangle}


Take the Rect class in the shapes module. Implement __rmul__, but in that case multiply the width of the rectangle.

Implement the addition of two rectangles. I think this should be defined only if one of the sides is the same,
but if you have an idea how to add two rectangualars of different sides, then go ahead, implement that.

Also implement all the comparision operators when comparing two rectangles, compare the area of the two. (like less-than)
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

## Exercise: imaginary numbers - complex numbers
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

* See [cmath](https://docs.python.org/library/cmath.html)

![](examples/advanced/complex_numbers.py)
![](examples/advanced/complex_numbers.out)


## Solution: Rectangle
{id: solution-oop-rectangle}

![](examples/oop/rect/shape2.py)
![](examples/oop/rect/test_rect.py)


## Solution: Implement a Gene inheritance model combining DNA
{id: solution-implement-a-gene-inheritance-model}

![](examples/advanced/gene_inheritance.py)

## Instance Attribute
{id: instance-attribute}

The attributes of the instance object can be set via 'self' from within the class.

![](examples/classes/person3.py)


## Use Python @propery to fix bad interface (the bad interface)
{id: property-fixing-bad-api-original}
{i: @property}

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



