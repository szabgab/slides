# Facade - simple interface to complex system

Facade, a structural design pattern. - Provide a simple interface (maybe a single class with few methods) to some complex system behind it.
This gives flexibility for the implementation of the complex system while users gain simplicity in using
it in certain subsets of operations.

```
os.path.basename, os.path.dirname are faced for os.path.split + indexing in the list
os.path.basename  = os.path.split()[-1]
os.path.split = split with os.sep
os.path.join(names) = os.sep.join(names)
os.path.isdir(path) = stat.S_ISDIR(os.stat(path))
```

* [](http://docs.python.org/library/os.path.html)
* [](http://docs.python.org/library/os.html)
* [](http://docs.python.org/library/stat.html)



