# Object Oriented Programming - OOP in Perl

When would you need to learn how to write Object Oriented code in Perl?

## Case 1.

You can accomplish a **lot** by using Perl in a procedural way, writing statements, functions, and even moving out some functions to modules. At one point you'll encounter a module that is itself written in the Object Oriented paradigm.
In order to use that module you'll need to learn a slightly different syntax. It is still not Object Oriented programming, but it is already using some classes and instances.

As you create more complex projects you might start to feel that you need a better organization of your data and functions. One such solution would be to convert some of your code to Object Oriented Perl.

## Case 2.

You get tasked to maintain a project that was already written in Object Oriented Perl and now you need to understand the internal working of the classes.


## Vocabulary

OOP or Object Oriented Programming is not the same in every programming language. Each implementation has its own features. However there is a mostly common vocabulary. I wrote "mostly" as even
the vocabulary used for various features of OOP might differ among programming languages. Let's see what are the words usually used:

* class (The blueprint of a collection of data and actions on that data. In python it is referred to as 'class object')
* instance (As in an instance of the class. Sometimes it is called an object. In python it is called an 'instance object'.)
* members (the collective name of attributes and methods)
* attributes (values, the data, basically internal variables)
* methods (actions, basically functions working with the data in the class or the instance. There are both class and instance methods)
* accessors (getters and setters, a subset of the methods that will allow the user to read or change the content of attributes)
* constructor (A specialized method to create the structure of an instance from a class.)
* initializer (A specialized method to fill the initial values of an instance after it was created by the constructor.)
* destructor (A method to clean up the mess after we are done using an instance.)
* inheritance (A way for a specialized class to reuse features of a more generic class.)
* polymorphism (The idea that different classes might have identically named attributes or behaviors that are somehow related.)
* encapsulation (It is the concept of hiding the internal parts of a class from the external world.)


* singleton (A design pattern to ensure that a class has only one instance.)


