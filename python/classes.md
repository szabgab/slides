# Classes - OOP - Object Oriented Programming
{id: python-classes}

## Why Object Oriented Programming?
{id: why-oop-in-python}

* Better encapsulation of intent.
* Integration between data and functionality (attributes and methods)
* Better modelling for some part of the world.
* Another level of code-reuse.
* Clearer separation between "usage" and "implementation". (Private data in some cases)
* Clearer connection between "classes" of things.
* In reality: avoid using "global".


## Generic Object Oriented Programming terms
{id: generic-oop-terms}

* OOP differs a lot among programming languages!
* Classes (blueprints)
* Objectes / instances (actual)
* Members: Attributes and Methods
* Attributes / Properties (variables - data)
* Methods (functions) (private, public, virtual)
* Inheritance (is a)
* Composition (has a)
* Constructor
* Destructor


## OOP in Python
{id: oop-examples-in-python}

* Everything is an object
* Numbers, strings, list, ... even classes are objects.
* Class objects
* Instance objects
* Nothing is private.


## OOP in Python (numbers, strings, lists)
{id: oop-examples-in-python-numbers}

{aside}
There are programming languages such as Java and C# that are Object Oriented languages where in order to do anything, even to print to the screen
you need to understand OOP and implement a class.

Python is Object Oriented in a different way. You can get by without creating your own classes for a very long time in your programming career,
but you are actually using features of the OOP nature of Python from the beginning.

In Python they say "everything is an object" and what they mean is that everything, including literal values such as numbers or strings, or variables holding
a list are instances of some class and that they all the features an instance has. Most importantly they have methods. Methods are just function that are used in
the "object.method()" notation instead of the "function( parameter )" notation.

Some of these methods change the underlying object (e.g. the append method of lists), some will return a copy of the object when the object is immutable. (e.g. the capitalize method of strings).
{/aside}


![](examples/oop/examples.py)


## OOP in Python (argparse)
{id: oop-examples-in-python-argparse}

{aside}
There are more complex OOP usage cases that you have surely encountered already in Python. Either while programming or in my course. For example parsing the command line arguments
using argparse.

Here we call the ArgumentParser() method of the argparse object to create an instance of the `argparse.ArgumentParser` class. Then we call the `add_argument` method a few times and the `parse_args` method.
This returns an instance of the `argparse.Namespace` class.

So in fact you have already used OOP quite a lot while using various already existing classes and instances of those classes.

Now we are going to learn how can you create your own classes.
{/aside}

![](examples/oop/examples_argparse.py)


## Create a class
{id: class-creation}

{i: class}
{i: __class__}
{i: __name__}
{i: dir}

{aside}
In order to create a class in Python you only need to use the `class` keyword with a new class-name.
Usually the first letter is capitalized.

In such a minimal class that does not do anything yet, Python still requires us to write some code.
{/aside}

![](examples/oop/empty_point.py)

## Create instance of class
{id: create-instance-of-class}

![](examples/oop/use_empty_point.py)

## Import module containing class
{id: import-module-containing-class}

{aside}
You probably want your classes to be reusabel by multiple programs, so it is better to put the class and your code using it in separate files
right from the beginning. In this example you can see how to do that importing the module and then using the dot notation to get to the class.
{/aside}

![](examples/oop/create/import_module.py)
![](examples/oop/create/shapes.py)


## Import class from module
{id: import-class-from-module}

{aside}
Alternatively you can import the class from the modue and then you can use the classname without any prefix.
{/aside}

![](examples/oop/create/import_class.py)

## Initialize instance (not a constructor)
{id: initialize-instance-of-class}
{i: __init__}

![](examples/oop/initialize_empty_point.py)


## Self is the instance
{id: self-is-the-instance}

Self is already the instance that will be returned

![](examples/oop/self_is_instance.py)


## Initialize a class - (not a constructor), attributes
{id: class-initialization}
{i: __init__}
{i: self}

{aside}
In Python we dont explicitely declare attributes so what people usually do is add a method calles `__init__`
and let that method set up the initial values of the insance-object.
{/aside}

![](examples/oop/attributes/shapes.py)

![](examples/oop/attributes/shapes2.py)

## Getters - access the attributes
{id: instance-getters}

![](examples/oop/attributes/getters.py)

## Setters - assign to the attributes
{id: instance-setters}

![](examples/oop/attributes/setters.py)


## Attributes are not special
{id: classe-attributes-from-outside}

* There is no automatic protection from this

![](examples/oop/attributes/color.py)

## Private attributes
{id: private-attributes}

![](examples/oop/attributes/private.py)

## Secret attributes
{id: secret-attributes}

* Primarily useful to ensure inheriting classes don't accidently overwrite attributes.

![](examples/oop/attributes/secret.py)


## Methods
{id: class-methods}

![](examples/oop/methods/shapes.py)
![](examples/oop/methods/point.py)


## Inheritance
{id: inheritance}
{i: super}

![](examples/oop/inheritance/shapes.py)
![](examples/oop/inheritance/circle.py)


## Inheritance - another level
{id: inheritance-level2}

![](examples/oop/inheritance/ball_shape.py)


## Modes of method inheritance
{id: modes-of-method-inheritance}

* Implicit
* Override
* Extend
* Delegate - Provide
* ---
* Composition


## Modes of method inheritance - implicit
{id: modes-of-method-inheritance-implicit}

Inherit method

![](examples/oop/inheritance/implicit.py)


## Modes of method inheritance - override
{id: modes-of-method-inheritance-override}

Replace method

![](examples/oop/inheritance/override.py)
![](examples/oop/inheritance/override.out)


## Modes of method inheritance - extend
{id: modes-of-method-inheritance-extend}
{i: super}

Extend method before or after calling original.

![](examples/oop/inheritance/extend.py)


## Modes of method inheritance - delegate - provide
{id: modes-of-method-inheritance-delegate-provide}

Let the child implement the functionality.

![](examples/oop/inheritance/delegate.py)

* Should we have a version of greet() in the Parent that throws an exception?
* Do we want to allow the creation of instance of the Parent class?
* Abstract Base Class (abc)


## Composition - Line
{id: composition-line}

When an object holds references to one or more other objects.

* [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)


![](examples/oop/composition/line.py)


## Some comments
{id: class-comments}

* There are no private attributes. The convention is to use leading underscore to communicate to other developers what is private.
* Using the name **self** for the current object is just a consensus.

## Exercise: Add move_rad to based on radians
{id: exercise-oop-move}

* From the **Python: Methods** take the examples/classes/methods/shapes.py and add a method called **move_rad(dist, angle)** that accpets a distance and an angle and moved the point accordingly.


```
delta_x = dist * cos(angle)
delta_y = dist * sin(angle)
```


## Exercise: Improve previous examples
{id: exercise-oop-balls}

* Take the previous example **Python: Inheritance - another level** and the example file called examples/classes/inheritance/ball_shape.py and change it so the **Ball** class will accept  **x, y, z, r**.
* Add a method called move to the new Ball class that will accept dx, dy, dz.
* Implement a method that will return the volume of the ball.


## Exercise: Polygon
{id: exercise-polygon}

* Implement a class representing a Point.
* Make the printing of a point instance nice.
* Implement a class representing a Polygon. (A list of points)
* Allow the user to "move a polygon" calling poly.move(dx, dy) that will change the coordinates of every point by (dx, dy)

![](examples/oop/composition/polygon-skeleton.py)


## Exercise: Number
{id: exercise-objects}

Turn the Number guessing game into a class. Replace every print statement with a call to an output method.
Do the same with the way you get the input.
Then create a subclass where you override these methods.
You will be able to launch the game with a hidden value you decide upon.
The input will feed a pre-defined list of values as guesses to the game
and the output methods will collect the values that the game prints in a list.


## Exercise: Library
{id: exercise-library}

Create a class hierarchy to represent a library that will be able to represent the following entities.

* Author (name, birthdate, books)
* Book (title, author, language, who_has_it_now?, is_on_waiting_list_for_whom?)
* Reader (name, birthdate, books_currently_lending)

Methods:

* write_book(title, language,) 

## Exercise: Bookexchange
{id: exercise-bookexchange}

It is like the library example, but instead of having a central library with books,
each person owns and lends out books to other people.


## Exercise: Represent turtle graphics
{id: exercise-turle-graphics}

There is a cursor (or turtle) in the x-y two-dimensional sphere. It has some (x,y) coordinates.
It can go forward n pixels. It can turn left n degrees. It can lift up the pencil or put it down.


## Solution - Polygon
{id: solution-polygon}

![](examples/oop/composition/polygon.py)

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


## Special methods
{id: special-class-methods}
{i: __str__}
{i: __repr__}

* `__str__`
* `__repr__`
* `__eq__`
* `__lt__`
* ...


## Stringify class
{id: class-stringification}
{i: __str__}
{i: __repr__}

* __repr__ "should" return Python-like code
* __str__ should return readable representation
* If __str__ does not exist, __repr__ is called instead.

![](examples/classes/stringification/point.py)
![](examples/classes/stringification/shapes.py)

* Class attributes
* Class methods
* Static methods


## Serialization of instances with pickle
{id: selialization-with-pickle}
{i: pickle}

![](examples/classes/serialization_with_pickle.py)

## Class in function
{id: class-in-function}

![](examples/oop/class_in_function.py)



