# Interactive shell
{id: interactive-shell}

## The Python interactive shell
{id: the-python-interactive-shell}
{i: len}


Type `python` without any arguments on the command line and
you'll get into the Interactive shell of Python.
In the interactive shell you can type:


![](examples/basics/interactive_shell.txt)


## REPL - Read Evaluate Print Loop
{id: python-repl}
{i: int}
{i: float}
{i: REPL}


A variable comes to existence the first time we assign a value to it.
It points to an object and that object knows about its type.


![](examples/basics/repl.txt)


## Using Modules
{id: using-modules}
{i: import}
{i: sys}
{i: version}
{i: executable}


Python has lots of standard (and not standard) modules. You can load one of them using the
`import` keyword. Once loaded, you can use functions from the module
or access its objects. For example the `sys` module has a `sys.version`
and a `sys.executable` variable.



```
>>> import sys
>>> sys.version
'2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]'
```

```
>>> sys.executable
'c:\\Python27\\python.exe'
```

You can also load specific object directly into your code.


```
>>> from sys import executable
>>> executable
'c:\\Python27\\python.exe'
```


To quit the interpreter call the `exit()` function.



```
>>> exit
Use exit() or Ctrl-Z plus Return to exit
```


The `import` binds the word sys to whatever it loaded from the file.




## Getting help
{id: getting-help}
{i: help()}
{i: dir()}
{i: import}

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


## Exercise: Interactive shell
{id: exercise-interactive-shell}

* Start the REPL and check the examples.
* Check the documentation in the REPL.




