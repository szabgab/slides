# Testing demo: doctest

* doctest
* $?
* %ERRORLEVEL%


The first way we are going to look at is using the "doctest" module. It is a very nice tool that allows us to test our code
and to also verify that our documentation is aligned with the code.
In addition to that, doctest is a standard module. It comes with every installation of Python so you don't need
to worry about installation.

The big drawback is that it is not really useful for anything complex.

So how does it work?

In Python if you add a string immediately after the declaration of the function - meaning the line immediately after the "def" statement -
that string becomes the documentation of the function. It can be a one-line string or a multi-line string using triple-quotes.

In the documentation you can write free text and you can also write examples as if one was using the interactive shell of Python.
For these examples we have code snippets preceded with 3 greater-than signs, the prompt of the in Python interactive shell. The line immediately
after that contains the result that you'd see if you actually typed in the expression into the interactive shell.

Doctest will read your source code, look at all the functions you have and for each function it will look at the documentation of the function.
If in the documentation it sees 3 greater-than signs then it will take the content of that line as code to be executed and the next line will be the
expected result. Doctest will execute each code snippet and compare it with the expected results. Effectively checking if the examples in
your documentation and the implementation are aligned.

We can run doctest in the following way: `python -m doctest mymath.py`. If all the tests pass, then this execution will print nothing.
This lack of positive feedback is a bit strange so you might want to check the so-called "exit code" of the execution. On Unix systems such as Linux and OSX,
you'd inspect the `$?` environment variable while on MS Windows you need to inspect the `%ERRORLEVEL%` variable. On all of these systems you can use
the `echo` command to inspect the variables. In either case 0 indicates success.


{% embed include file="src/examples/testing-demo/doctest_first/mymath.py" %}

```
$ python -m doctest mymath.py
$ echo $?
0
```

```
> python -m doctest mymath.py
> echo %ERRORLEVEL%
0
```


