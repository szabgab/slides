# Design Patterns
{id: design-patterns}

## What are Design Patterns?
{id: what-are-design-patterns}

{aside}

Not all the Design Patterns discussed for Java or C++ are interesting, relevant or even needed in Python.
Design Patterns are formal descriptions of how people do things, and not how you should do things.
The formal description makes it easy to talk about them.

Some of the DPs exists to overcome problems in that specific language.
Oher DPs are more general, solving classes of problem that are generic.
{/aside}


## Don't replace built-in objects
{id: dont-replace-built-in-objects}
![](examples/patterns/replace_print.py)


```
pip install flake8-builtins
flake8 --ignore=   replace_print.py

replace_print.py:3:1: A001 "print" is a python builtin and is being shadowed, consider renaming the variable
```


## Facade - simple interface to complex system
{id: dp-facade}

{aside}

Facade, a structural design pattern. - Provide a simple interface (maybe a single class with few methods) to some complex system behind it.
This gives flexibility for the implementation of the complex system while users gain simplicity in using
it in certain subsets of operations.
{/aside}


```
os.path.basename, os.path.dirname are faced for os.path.split + indexing in the list
os.path.basename  = os.path.split()[-1]
os.path.split = split with os.sep
os.path.join(names) = os.sep.join(names)
os.path.isdir(path) = stat.S_ISDIR(os.stat(path))
```

* <a href="http://docs.python.org/2/library/os.path.html"></a>
* <a href="http://docs.python.org/2/library/os.html"></a>
* <a href="http://docs.python.org/2/library/stat.html"></a>



## Monkey Patching
{id: monkey-patching}

```
import real_class
class faker(object): pass
fake = faker
real_class.time = fake
fake.sleep =
fake.time =
```

* handy in emergencies
* easily abused for NON-emergencies - gives dynamic languages a bad name
* subtle hidden "communication" via secret obscure pathways (explicit is better)

![](examples/classes/monkey.py)



## Creation DPs "Just One"
{id: just-one-design-pattern}

we want just one instance to exist


* Singleton - subclassing can never be really smooth
* Use a module instead of a class (no inheritance, no special methods)
* make just one instance (self discipline, no enforcement), need to decide to "when" (in which part if the code) to make it
* monostate (borg)



## Singleton
{id: singleton}

```
   class Singleton(object):
   def __new__(cls, *a, **kw):
       if not hasattr(cls, '_inst'):
           cls._inst = super(Singleton, cls).__new__(*a, **kw)
       return cls._inst
```

the problem


```
   class Foo(Singleton): pass
   class Bar(Foo): pass
   f = Foo()
   b = Bar()
   # what class is b now? is that a Bar or a Foo instance?
```


## Monostate (Borg)
{id: monostate-design-pattern}

<a href="http://c2.com/cgi/wiki?MonostatePattern"></a>


```
class Monostate(object):
    _shared_state = {}
    def __new__(cls, *a, **kw):
        obj = super(Monostate, cls).__new__(*a, **kw)
        obj.__dict__ = _shared_state
        return obj

class Foo(Monostate) pass
class Bar(Foo) pass
f = Foo()
b = Bar()
```


Better than singleton, data overriding to the rescue:
But what if two calls to the constructor provide different initial data?




## Dispatch table
{id: dispatch-table}
![](examples/patterns/dispatch_table.py)



