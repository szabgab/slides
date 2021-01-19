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
{i: object}
{i: __class__}
{i: __name__}
{i: dir}

![](examples/classes/ppl.py)
![](examples/classes/ppl.out)

In Python 2.x classes needed to inherit from 'object' in order to become 'new style' classes.



## Import module containing class
{id: import-module-containing-class}

![](examples/classes/pplx.py)
![](examples/classes/import_module.py)
![](examples/classes/import_module.out)


## Import class from module
{id: import-class-from-module}

![](examples/classes/pplx.py)
![](examples/classes/import_class.py)


## Initialize a class - constructor, attributes
{id: class-initialization}
{i: __init__}
{i: self}
![](examples/classes/initialization/ppl.py)


## Attributes are not special
{id: classe-attributes-from-outside}
![](examples/classes/attributes/ppl.py)


## Create Point class
{id: create-class-point}
![](examples/classes/create/point.py)
![](examples/classes/create/shapes.py)


## Initialize a class - constructor, attributes
{id: class-initialization-point}
{i: __init__}
{i: self}
![](examples/classes/initialization/point.py)
![](examples/classes/initialization/shapes.py)


## Methods
{id: class-methods}
![](examples/classes/methods/point.py)
![](examples/classes/methods/shapes.py)


## Stringify class
{id: class-stringification}
{i: __str__}
{i: __repr__}

* __repr__ "should" return Python-like code
* __str__ should return readable representation
* If __str__ does not exist, __repr__ is called instead.

![](examples/classes/stringification/point.py)
![](examples/classes/stringification/shapes.py)


## Inheritance
{id: inheritance}
![](examples/classes/inheritance/shapes.py)
![](examples/classes/inheritance/circle.py)


## Inheritance - another level
{id: inheritance-level2}
![](examples/classes/inheritance/ball_shape.py)


## Modes of method inheritance
{id: modes-of-method-inheritance}

* Implicit
* Override
* Extend
* Delegate - Provide


## Modes of method inheritance - implicit
{id: modes-of-method-inheritance-implicit}

Inherit method

![](examples/classes/inheritance/implicit.py)


## Modes of method inheritance - override
{id: modes-of-method-inheritance-override}

Replace method

![](examples/classes/inheritance/override.py)
![](examples/classes/inheritance/override.out)


## Modes of method inheritance - extend
{id: modes-of-method-inheritance-extend}
{i: super}

Extend method before or after calling original.

![](examples/classes/inheritance/extend.py)


## Modes of method inheritance - delegate - provide
{id: modes-of-method-inheritance-delegate-provide}

Let the child implement the functionality.

![](examples/classes/inheritance/delegate.py)

* Should we have a version of greet() in the Parent that throws an exception?
* Do we want to allow the creation of instance of the Parent class?
* Abstract Base Class (abc)



## Composition - Line
{id: composition-line}

When an object holds references to one or more other objects.

* [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)


![](examples/classes/composition/line.py)


## Some comments
{id: class-comments}

* There are no private attributes. The convention is to use leading underscore to communicate to other developers what is private.
* Using the name **self** for the current object is just a consensus.



## Class in function
{id: class-in-function}

![](examples/classes/class_in_function.py)



## Serialization of instances with pickle
{id: selialization-with-pickle}
{i: pickle}

![](examples/classes/serialization_with_pickle.py)


## Quick Class definition and usage
{id: quick-class-definition}

![](examples/classes/quick.py)


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

![](examples/classes/composition/polygon-skeleton.py)


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

![](examples/classes/composition/polygon.py)

