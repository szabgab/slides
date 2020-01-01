# Modules
{id: python-modules}

## Before modules
{id: in-one-file}
![](examples/functions/my_calculator_one_file.py)



## Create modules
{id: create-modules}

{aside}
A module is just a Python file with a set of functions that us usually not used by itself. For example the "my_calculator.py".
{/aside}

![](examples/functions/my_calculator.py)

{aside}

A user made module is loaded exactly the same way as the built-in module.
The functions defined in the module are used as if they were methods.
{/aside}
![](examples/functions/add.py)



{aside}

We can import specific functions to the current name space (symbol table) and then we don't need to prefix it with the name of
the file every time we use it. This might be shorter writing, but if we import the same function name from two different
modules then they will overwrite each other. So I usually prefer loading the module as in the previous example.
{/aside}
![](examples/functions/add_from.py)


## path to load modules from - The module search path
{id: path-to-load-modules-from}
{i: PYTHONPATH}
{i: .pth}

1. The directory where the main script is located.
1. The directories listed in PYTHONPATH environment variable.
1. Directories of standard libraries.
1. Directories listed in .pth files.
1. The site-packages home of third-party extensions.



## sys.path - the module search path
{id: sys-path}
![](examples/package/syspath.py)

```
['/Users/gabor/work/training/python/examples/package',
 '/Users/gabor/python/lib/python2.7/site-packages/crypto-1.1.0-py2.7.egg',
 ...
 '/Library/Python/2.7/site-packages', '/usr/local/lib/python2.7/site-packages']
[Finished in 0.112s]
```


## Flat project directory structure
{id: project-directory-structure}

{aside}

            If our executable scripts and our modules are all in the same directory then we don't have to worry ad the directory of the script is included in the list of places
            where "import" is looking for the files to be imported.
{/aside}

```
project/
     script_a.py
     script_b.py
     my_module.py
```


## Absolute path
{id: absolute-path}

{aside}

    If we would like to load a module that is not installed in one of the standard locations, but we know where it is located on our disk,
    we can set the "sys.path" to the absolute path to this directory. This works on the specific computer, but if you'd like to distribute
    the script to other computers you'll have to make sure the module to be loaded is installed in the same location or you'll
    have to update the script to point to the location of the module in each computer. Not an ideal solution.
{/aside}
![](examples/modules/load_from_absolute_path.py)




## Relative path
{id: relative-path}
{i: __file__}
{i: dirname}
{i: abspath}
{i: sys.path}

```
../project_root/
     bin/relative_path.py
     lib/my_module.py
```

{aside}
We can use a directory structure that is more complex than the flat structure we had earlier. In this case the location of the modules relatively to the scripts
    is fixed. In this case it is "../lib". We can compute the relative path in each of our scripts. That will ensure we pick up the right module every time we run the script.
        Regardless of the location of the whole project tree.
{/aside}
![](examples/sys/lib/my_module.py)
![](examples/sys/bin/relative_path.py)



## Traverse directory tree - list directories recursively
{id: travers-directory-tree}
![](examples/os/traverse_tree.py)



## Python modules are compiled
{id: compile-python-modules}
{i: pyc}
{i: __pycache__}


When libraries are loaded they are automatically compiled to <b>.pyc</b> files.
This provides moderate code-hiding and load-time speed-up. Not run-time speed-up.
Starting from Python 3.2 the pyc files are saved in the <b>__pycache__</b> directory.




## How "import" and "from" work?
{id: how-import-works}
{i: import}

1. Find the file to load.
1. Compile to bytecode if necessary and save the bytecode if possible.
1. Run the code of the file loaded.
1. Copy names from the imported module to the importing namespace.



## Runtime loading of modules
{id: runtime-loading-of-modules}
![](examples/functions/mygreet.py)
![](examples/functions/runtime_loading.py)


## Conditional loading of modules
{id: conditional-loading-of-modules}
![](examples/functions/conditional_loading.py)



## Duplicate importing of functions
{id: duplicate-importing-of-functions}
![](examples/functions/duplicate_add_from_module.py)

The second declaration silently overrides the first declaration.


[pylint](http://www.pylint.org/) can find such problems, along with a bunch of others.




## Script or library
{id: python-script-or-library}
{i: __main__}
{i: __name__}

{aside}
We can have a file with all the functions implemented and then launch the run() function only if the file was executed as a stand-alone script.
{/aside}

![](examples/functions/mymodule.py)

```
$ python mymodule.py
Name space in mymodule.py  __main__
run in  __main__
```



## Script or library - import
{id: python-script-or-library-import}

{aside}
If it is imported by another module then it won't run automatically. We have to call it manually.
{/aside}

![](examples/functions/import_mymodule.py)

```
$ python import_mymodule.py
Name space in mymodule.py  mymodule
Name space in import_mymodule.py  __main__
run in  mymodule
```


## Script or library - from import
{id: python-script-or-library-from-import}
![](examples/functions/import_from_mymodule.py)

```
$ python import_from_mymodule.py
Name space in mymodule.py  mymodule
Name space in import_mymodule.py  __main__
run in  mymodule
```


## assert to verify values
{id: assert}
{i: assert}
![](examples/functions/raise_exception.py)
![](examples/functions/assert.py)


## mycalc as a self testing module
{id: self-testing-module}
{i: __file__}
![](examples/functions/use_mycalc.py)

```
$ python use_mycalc.py
42
```
![](examples/functions/mycalc.py)

```
$ python mycalc.py
Self testing  mycalc.py
```


## doctest
{id: doctest}
{i: doctest}
![](examples/functions/fibonacci_doctest.py)

```
python -m doctest fibonacci_doctest.py
```

```
$python examples/functions/fibonacci_doctest.py

**********************************************************************
File ".../examples/functions/fibonacci_doctest.py", line 12, in __main__.fib
Failed example:
    fib(11)
Expected:
    89
Got:
    'bug'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.fib
***Test Failed*** 1 failures.
```

[doctest](https://docs.python.org/3/library/doctest.html)




## Scope of import
{id: scope-of-import}
![](examples/functions/mydiv.py)
![](examples/functions/division.py)

{aside}
The importing of functions, and the changes in the behavior of the compiler are file specific.
In this case the change in the behavior of division is only visible in the division.py script, but not in the mydiv.py module.
{/aside}


## Export import
{id: export-import}
{i: __all__}
{i: import}
{i: from}

* from mod import a,b,_c  - import 'a', 'b', and '_c' from 'mod'
* from mod import *  - import every name listed in __all__ of 'mod' if __all__ is available.
* from mod import *  - import every name that does NOT start with _ (if __all__ is not available)
* import mod - import 'mod' and make every name in 'mod' accessible as 'mod.a', and 'mod._c'

![](examples/modules/my_module.py)
![](examples/modules/x.py)
![](examples/modules/y.py)


## Export import with __all__
{id: import-with-all}
{i: __all__}
![](examples/modules/my_module2.py)
![](examples/modules/z.py)


## import module
{id: import-module}
![](examples/modules/q.py)



## deep copy list
{id: deep-copy-list}

![](examples/modules/copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
```

![](examples/modules/shallow_copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


![](examples/modules/deep_copy_list.py)

```
[{'name': 'Jane', 'email': 'joe@examples.com', 'phone': '1234'}, {'name': 'Mary', 'email': 'mary@examples.com'}, {'name': 'George'}]
[{'name': 'Joe', 'email': 'joe@examples.com'}, {'name': 'Mary', 'email': 'mary@examples.com'}]
```


## deep copy dictionary
{id: deep-copy-dictionary}

![](examples/modules/copy_dictionary.py)

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
```



<a href="https://docs.python.org/2/library/copy.html#copy.deepcopy">deepcopy</a>



![](examples/modules/deep_copy_dictionary.py)

```
{'name': 'Foo Bar', 'grades': {'math': 90, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George'], 'email': 'foo@bar.com'}
{'name': 'Foo Bar', 'grades': {'math': 70, 'art': 100}, 'friends': ['Mary', 'John', 'Jane', 'George']}
```



## Execute at import time
{id: execute-at-import-time}
![](examples/modules/execute_import_time/code.py)
![](examples/modules/execute_import_time/lib.py)
![](examples/modules/execute_import_time/code.out)


## Import multiple times
{id: import-multiple-times}
![](examples/modules/import_multiple_times/code.py)
![](examples/modules/import_multiple_times/one.py)
![](examples/modules/import_multiple_times/two.py)
![](examples/modules/import_multiple_times/common.py)
![](examples/modules/import_multiple_times/code.out)



## Exercise: Number guessing
{id: exercise-number-guessing-game-with-functional}


Take the number guessing game from the earlier chapter and move the internal while() loop
to a function.




Once that's done, move the function out to a separate file and use it as a module.




## Exercies: Scripts and modules
{id: exercise-functional-scripts-and-modules}


Take the number guessing game: if I run it as a script execute the whole game with repeated hidden numbers.
If I load it as a module, then let me call the function that runs a single game with one hidden number.
We should be able to even pass the hidden number as a parameter.




## Exercise: Module my_sum
{id: exercise-module-sum}

* Create a file called "my_simple_math.py" with three functions: "div(a, b)", "add(a, b)", that will divide and add the two numbers respectively.
* Add another two functions called "test_div" and "test_add" that will test the above two functions using assert.
* Add code that will run the tests if someone execute "python my_simple_math.py" running the file as if it was a script.
* Create another file called "use_my_simple_math.py" that will use the functions from "my_math" module to calculate  2 + 5 * 7
* Make sure when you run "python use_my_simple_math.py" the tests won't run.
* Add documentation to the "add" and "div" functions to examples that can be used with doctest.


* Can you run the tests when the file is loaded as a module?




## Exercise: Convert your script to module
{id: exercise-convert-your-script-to-module}

* Take one of your real script (from work). Create a backup copy.
* Change the script so it can be import-ed as a module and then it won't automatically execute anything, but that it still works when executed as a script.
* Add a new function to it called 'self_test' and in that function add a few test-cases to your code using 'assert'.
* Write another script that will load your real file as a module and will run the 'self_test'.
* Let me know what are the dificulties!



## Exercise: Add doctests to your own code
{id: exercise-add-doctests-to-your-own-code}

* Pick a module from your own code and create a backup copy. (from work)
* Add a function called 'self_test' that uses 'assert' to test some of the real functions of the module.
* Add code that will run the 'self_test' when the file is executed as a script.
* Add documentation to one of the functions and convert the 'assert'-based tests to doctests.
* Convert the mechanism that executed the 'self_test' to run the doctests as well.
* Let me know what are the dificulties!



## Solution: Module my_sum
{id: solution-module-sum}
![](examples/modules/my_simple_math.py)
![](examples/modules/use_my_simple_math.py)



