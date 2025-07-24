# Modules



When we program in Python we basically have 3 main pieces. The base-language itself. A set of standard modules. A set of 3rd party modules.

All the modules provide additional functionality to the base-language and without them we would not be able to do much. The standard modules
come installed with Python, the 3rd party modules we need to install. Once installed however they behave in the same way. We need to `import`
them and then we can use them. We'll discuss these even more later, but we already would like to use some so let's see some basic ideas.

I know we already used the `math` module in the solution of the earlier exercises, but some people might have missed those.

In this example we `import` the `sys` module that contains various attributes and operations related to the Python system. (There is another module
called `os` that provides functionality related to the Operating System.)

A few examples:

The `executable` attribute pointing to where the currently running Python executable is located. On MS Windows this will be a path to a python.exe file.

`platform` is going to be `win32` on any Windows machine.

We are going to discuss the whole `sys.argv` thing a lot more, but for now look `sys.argv[0]` contains path to the current Python file.

`sys.version_info` contains the version information about the currently running Python.
Specifically `sys.version_info.major` contains the major version number which 3 for Python 3 and 2 for Python 2.
If really needed, you could use this to recognize when someone is trying to run your program on an unsupported version of Python.

These were all attributes that contain some fixed value.

There is also the `getsizeof` function that comes with the `sys` module. You know it is a function because you see a pair of parentheses
at the end. The attributes above did not have parentheses. Functions do something. This specific function calculates the number of bytes
being used by an object.

You can see an integer (both 1 and 42) use 28 bytes.

A floating point number uses 24 bytes.

An empty string uses 49 bytes.

Then each character takes another byte. (Actually this is only true in the case of Latin letters, but let's not get ahead of ourselves.)


* The documentation of the [sys](https://docs.python.org/library/sys.html) module.

{% embed include file="src/examples/basics/modules.py" %}


