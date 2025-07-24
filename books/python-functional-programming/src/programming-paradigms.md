# Programming Paradigms

There are a number of [programming paradigms](https://en.wikipedia.org/wiki/Programming_paradigm) or "styles of code" that can be categorized in a number of ways. The most popular, most commonly used ones
are the following:

* Procedural
* Object Oriented
* Declarative
* Functional

**Procedural** programming is the most common one, putting one statement after the other. Using functions (that are called procedures in some languages). Maybe splitting out some code to libraries (aka. modules).
C is probably the most popular procedural language.

**Object Oriented** is when you divide your code into classes. Create instances of the classes. Internally, inside the classes, you still have functions (procedures), though these are now called methods.
Java is probably the most popular object oriented language.

**Declarative** is very different. SQL is probably the most well-known example. Here you describe the type of result you are looking for and the engine behind figures out how to go about to get what you asked for.

**Functional** is a style in which you basically write lots of functions. Haskell might be the most well-known example.

----

In Python we can use Procedural, Object Oriented, and Functional paradigms. It is also rather different from the other languages. You don't pick one paradigm, you just write code in hopefully the most appropriate way for the given
task and given environment.

When you write `len(text)` this is procedural. You call the `len` function (procedure) on a variable called `text`.

When you write `text.lower()` this is basically Object Oriented, even though you don't yet defined your own classes and instances. You are using the fact that `text` is an instance object and it has a method called `lower`.

When using `map`, `filter`, or list-comprehension you use the functional paradigm of Python.

So you see you probably have already use some of the functional aspects of Python even without realizing it.

In the next few pages we'll show a lot of examples in Python using the functional paradigm and by the end of this booklet you'll understand how things work much better and you'll feel a lot more comfortable writing these constructs.







