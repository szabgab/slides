# Getting help

* help()
* dir()
* import

```
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()    - entering an internal shell:
...
help> dir     - explains about the dir command.  Navigate using SPACE/ENTER/q
help> Ctrl-D  - to quite, (Ctrl-Z ENTER on Windows)
>>> help(dir) - the same explanation as before

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> dir("")   - list of string related methods
['__add__', '__class__', ... 'upper', 'zfill']

>>> dir(1)    - list of integer related methods
['__abs__', '__add__', ... 'numerator', 'real']

>>> dir(__builtins__)
...                   - functions available in python

>>> help(abs)         - exlain how abs() works
>>> help(sum)
>>> help(zip)
>>> help(int)
>>> help(str)

>>> help("".upper)   - explain how the upper method of strings work

>>> import sys
>>> dir(sys)
>>> help(sys)
>>> help(sys)
>>> help(sys.path)
>>> help(sys.path.pop)
```


