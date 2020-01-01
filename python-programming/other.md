# Other slides
{id: other}

## Other slides
{id: other-slides}


Some slides that used to be part of the material and they might return to be there, but for now they were parked here.




## Atom for Python
{id: atom-for-python}

{aside}

Some details about the Atom editor. You can freely skip this part. Personally I don't use it now.
{/aside}

* [Atom](https://atom.io/)


Autocomplete


* apm install autocomplete-python


Autocomplete


* easy_install jedi
* apm install autocomplete-plus-python-jedi


Linter


* easy_install flake8
* easy_install flake8-docstrings
* apm install linter
* apm install linter-flake8


[source](http://www.marinamele.com/install-and-configure-atom-editor-for-python)



## IDLE - Integrated DeveLopment Environment
{id: idle}
{i: IDLE}

* Python shell
* Better editing
* Limited debugger
* <programlisting>c:\Python27\Lib\idlelib\idle.bat</programlisting>
* **C:\Users\Gabor\AppData\Local\Programs\Python\Python35\Lib\idlelib\idle.bat**



## sh-bang - executable on Linux/Apple
{id: sh-bang}
![](examples/basics/hello_ex.py)

* The first line staring with # is needed if you want to have a file that can be executed without explicitly typing in python as well.
* Make your file executable: **chmod u+x hello_ex.py**
* Run like: **./hello_ex.py**
* In order to run it as **hello_ex.py** in needs to be located in one of the directories listed in the **PATH** environment variable.



## Strings as Comments
{id: strings-as-comments}
{i: '''}

{aside}

# marks single line comments.
There are no real multi-line comments in Python, but we can use triple-quots to
create multi-line strings and if they are not part of another statement,  they will be
disregarded by the Python interpreter. Effectively creating multi-line comments.
{/aside}
![](examples/basics/string_comments.py)


## pydoc
{id: pydoc}


If you really want it, you can also read some of the documentation on the command line, but unless you are locked up some place without Internet connection,
I don't recommend this.




Type <command>pydoc</command>. On Windows, you might need to create the following file and put it in a directory in your PATH. (see <command>echo %PATH%</command>)


![](examples/basics/pydoc.bat)


## How can I check if a string can be converted to a number?
{id: is-number}
{i: int}
{i: float}
{i: is_int}
{i: is_float}


There is no is_int, we just need to try to convert and catch the exception, if there is one.


![](examples/basics/is_number.py)


## Spyder Intro
{id: spyder-intro}

* iPython console (bottom right)
* Spyder-Py2 / Preferences / Console / Advanced Settings 
* Save the file (Ctrl-S / Command-S)
* Run/Run  (F5)
* F9   - execute selected text (e.g. we can eecute a function definition after we've changed it)
* TAB for autocomple names of already existing variables.


```
print("abc")
"abc".          shows the available methods.
"abc".center    Command-I will explain what is "center"
```


## Interactive Debugging
{id: interactive-debugging}
![](examples/other/interact.py)


## Parameter passing
{id: parameter-passing}
![](examples/basics/parameter_passing.py)

```
Hello Foo!!!!
```


## Command line arguments and main
{id: command-line-arguments-and-main}
![](examples/basics/argv_main.py)

Run as **python argv.py Foo**



Later we'll see the <command>argparse</command> module that can handle command line arguments in a better way.




## Infinite loop
{id: infinite-loop}
![](examples/strings/infinite_loop.py)


## break
{id: break}
{i: break}
![](examples/strings/break.py)

```
0
1
2
3
4
5
6
done
```


## continue
{id: continue}
{i: continue}
![](examples/strings/continue.py)

```
1
2
3
8
9
10
```


## While with many conditions
{id: while-many-conditions}
![](examples/strings/while_many_conditions.py)


## while loop with many conditions
{id: infinite-while-many-conditions}
![](examples/strings/infinite_while_many_conditions.py)


## Format with conversion (stringifiation with str or repr)
{id: format-with-conversion}

Adding !s or !r in the place-holder we tell it to cal the str or repr
method of the object, respectively.



* repr (__repr__) Its goal is to be unambiguous
* str (__str__) Its goal is to be readable
* The default implementation of both are useless
* Suggestion
* [Difference between __str__ and __repr__](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

![](examples/strings/format_no_conversion.py)
![](examples/strings/format_conversions.py)


## Name of the current function in Python
{id: name-of-the-current-function}
{i: inspect}
{i: currentframe}
{i: stack}
![](examples/advanced/name_of_current_function.py)


## Name of the caller function in Python
{id: name-of-the-caller-function}
{i: inspect}
{i: stack}
![](examples/advanced/name_of_caller_function.py)


## Stack trace in Python using inspect
{id: stack-trace-using-inspect}
{i: inspect}
{i: stack}
![](examples/advanced/stack_trace.py)
![](examples/advanced/stack_trace.out)


## Module Fibonacci
{id: pytest-fibo}
![](examples/pytest/fibo.py)


## PyTest - assertion
{id: pytest-assertion}
![](examples/pytest/test_fibonacci_ok.py)
![](examples/pytest/test_fibonacci_ok.out)


## PyTest - failure
{id: pytest-fibonacci-failure}
![](examples/pytest/test_fibonacci.py)
![](examples/pytest/test_fibonacci.out)


## PyTest - list
{id: pytest-list}
![](examples/pytest/test_fibo.py)
![](examples/pytest/test_fibo.out)


## SAX with coroutine
{id: sax-coroutine}
![](examples/xml/sax_coroutine.py)


copied from <a href="http://stackoverflow.com/questions/8873643/how-to-return-data-from-a-python-sax-parser">Stack Overflow</a>
based on <a href="http://www.dabeaz.com/coroutines/">coroutines</a>


![](examples/xml/cosax.py)


## Getting the class name of an object
{id: class-name}
{i: __class__}
{i: __name__}
{i: type}

How to find out which class an object (instance) belongs to?

![](examples/other/class.py)


## Inheritance - super
{id: inheritance-call-super}

{aside}
We can also call super() passing a different class name
{/aside}

![](examples/classes/inheritance/ball_shape2.py)


## Inheritance - super - other class
{id: inheritance-bad-super}

{aside}
We cannot pass any class name to super()
{/aside}

![](examples/classes/inheritance/bad_shapes.py)



## iterator - pairwise
{id: iterator-pairwise}
![](examples/iterators/pairwise_manual.py)


## iterator - grouped
{id: iterator-grouped}
![](examples/iterators/grouped_manual.py)


## itertools - groupby
{id: itertools-groupby}

Group elements

![](examples/iterators/groupby.py)



