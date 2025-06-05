# Modules
{id: modules}


## Goal of having modules
{id: goal-of-having-modules}

* Code reuse: Allow multiple script to reuse the same function without copying the code.
* Better code design.
* Separation of concerns: Functions dealing with one subject are grouped together in one module.

## Before modules
{id: in-one-file}

{aside}
Let's take a very simple script that has a single, and very simple function in it.
{/aside}

![](examples/modules/my_calculator_one_file.py)

## Create modules
{id: create-modules}

{aside}
A module is just a Python file with a set of functions that us usually not used by itself. For example the "my_calculator.py".
{/aside}

![](examples/modules/my_calculator.py)

{aside}
A user made module is loaded exactly the same way as the built-in module.
The functions defined in the module are used as if they were methods with the dot-notation.
{/aside}

![](examples/modules/add.py)


{aside}
We can import specific functions to the current name space (symbol table) and then we don't need to prefix it with the name of
the file every time we use it. This might be shorter writing, but if we import the same function name from two different
modules then they will overwrite each other. So I usually prefer loading the module as in the previous example.
{/aside}

![](examples/modules/add_from.py)

* Using with an alias

![](examples/modules/add_as.py)

## path to load modules from - The module search path
{id: path-to-load-modules-from}
{i: PYTHONPATH}
{i: .pth}

{aside}
There are several steps Python does when it searches for the location of a file to be imported, but the most important
one is what we see on the next page in sys.path.
{/aside}

1. The directory where the main script is located.
1. The directories listed in PYTHONPATH environment variable.
1. Directories of standard libraries.
1. Directories listed in .pth files.
1. The site-packages home of third-party extensions.


## sys.path - the module search path
{id: sys-path}
{i: sys}
{i: path}

![](examples/package/syspath.py)

```
['/Users/gabor/work/training/python/examples/package',
 '/Users/gabor/python/lib/python2.7/site-packages/crypto-1.1.0-py2.7.egg',
 ...
 '/Library/Python/2.7/site-packages', '/usr/local/lib/python2.7/site-packages']
[Finished in 0.112s]
```


## Project directory layouts
{id: project-directory-layouts}

* Flat project
* Absolute path
* Relative path
* Using submodules

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
have to update the script to point to the location of the module in each computer. This is not an ideal solution.
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

![](examples/project_root/lib/my_module.py)
![](examples/project_root/bin/relative_path.py)


## Relative path explained
{id: relative-path-explained}

```
../project_root/
     bin/relative_path_explained.py
     lib/my_module.py
```

![](examples/project_root/bin/relative_path_explained.py)
![](examples/project_root/bin/relative_path_explained.out)

## Submodules
{id: submodules}

```
aproject/
    app.py
    mymodules/math.py
```

![](examples/aproject/app.py)
![](examples/aproject/mymodules/math.py)


## Python modules are compiled
{id: compile-python-modules}
{i: pyc}
{i: __pycache__}

When libraries are loaded they are automatically compiled to `.pyc` files.
This provides moderate code-hiding and load-time speed-up. Not run-time speed-up.
Starting from Python 3.2 the pyc files are saved in the `__pycache__` directory.


## How "import" and "from" work?
{id: how-import-works}
{i: import}

1. Find the file to load.
1. Compile to bytecode if necessary and save the bytecode if possible.
1. Run the code of the file loaded.
1. Copy names from the imported module to the importing namespace.

## Execute at import time
{id: execute-at-import-time}

![](examples/modules/execute_import_time/code.py)
![](examples/modules/execute_import_time/lib.py)
![](examples/modules/execute_import_time/code.out)


## Runtime loading of modules
{id: runtime-loading-of-modules}

{aside}
The import statements in Python are executed at the point where they are located in the code.
If you have some code before the import statement (print Start running) it will be executed before the importing starts.

During the importing any code that is outside of functions and classes in the imported module is executed. (print Loading mygreet).

Then you can call functions from the module (print Hello World).

Or call code that is in the importing program (print DONE).
{/aside}

![](examples/modules/mygreet.py)
![](examples/modules/load_mygreet.py)
![](examples/modules/runtime_loading.py)


## Conditional loading of modules
{id: conditional-loading-of-modules}

![](examples/modules/conditional_loading.py)


## What is in our namespace?
{id: what-is-in-your-namespace}

![](examples/modules/what_is_in_the_namespace.py)
![](examples/modules/what_is_in_the_namespace.out)

## Runtime import
{id: runtime-import}

* We can use the name of a module that comes from an expression


## Duplicate importing of functions
{id: duplicate-importing-of-functions}

![](examples/modules/duplicate_add_from_module.py)

The second declaration silently overrides the first declaration.


[pylint](http://www.pylint.org/) can find such problems, along with a bunch of others.

```
pylint --disable=C  duplicate_add_from_module.py
```

![](examples/modules/duplicate_add_from_module_lint.out)

## Duplicate importing of functions - solved
{id: duplicate-importing-of-functions-solved}


![](examples/modules/duplicate_add_from_module_solved.py)

## Script or library
{id: python-script-or-library}
{i: __main__}
{i: __name__}

{aside}
We can have a file with all the functions implemented and then launch the run() function only if the file was executed as a stand-alone script.
{/aside}

![](examples/modules/mymodule.py)

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

![](examples/modules/import_mymodule.py)

```
$ python import_mymodule.py
Name space in mymodule.py  mymodule
Name space in import_mymodule.py  __main__
run in  mymodule
```


## Script or library - from import
{id: python-script-or-library-from-import}
![](examples/modules/import_from_mymodule.py)

```
$ python import_from_mymodule.py
Name space in mymodule.py  mymodule
Name space in import_mymodule.py  __main__
run in  mymodule
```


## Scope of import
{id: scope-of-import}

![](examples/modules/mydiv.py)
![](examples/modules/division.py)

{aside}
The importing of functions, and the changes in the behavior of the compiler are file specific.
In this case the change in the behavior of division is only visible in the division.py script, but not in the mydiv.py module.
{/aside}



## Import multiple times
{id: import-multiple-times}

![](examples/modules/import_multiple_times/code.py)
![](examples/modules/import_multiple_times/one.py)
![](examples/modules/import_multiple_times/two.py)
![](examples/modules/import_multiple_times/common.py)
![](examples/modules/import_multiple_times/code.out)


## Do not import *
{id: do-not-import-everything}

* Despite the examples you can use in various places, I'd recommend never to import "everything" using `*`.

```
from one import *
from two import *


run()
```

* Where does `run()` come from?
* What if both moduldes have the `run()` function? Then the order of the import will be important.
* What if the `one` has the `run()` function, but a new version of `two` also adds one?


## Exercise: Number guessing
{id: exercise-number-guessing-game-with-modules}

Take the number guessing game and move the function out to a separate file and use it as a module.

## Exercies: Scripts and modules
{id: exercise-functional-scripts-and-modules}

Take the number guessing game:

If I run it as a script like this: `python game.py` then execute the whole game. Allow the user to play several games each time with a new hidden number.

If I load it as a module, then let me call the function that runs a single game with one hidden number. For example:

```
import game

game.run_game()   # will generate a new hidden number
```

We should be able to even pass the hidden number as a parameter. Like this:

```
import game

game.run_game(42)
```

## Exercise: Module my_sum
{id: exercise-module-sum}

* Create a file called `my_simple_math.py` with two functions: `div(a, b)`, `add(a, b)`, that will divide and add the two numbers respectively.
* Add another two functions called `test_div` and `test_add` that will test the above two functions using assert.
* Add code that will run the tests if someone execute `python my_simple_math.py` running the file as if it was a script.
* Create another file called `use_my_simple_math.py` that will use the functions from `my_math` module to calculate  2 + 5 * 7
* Make sure when you run `python use_my_simple_math.py` the tests won't run.
* Add documentation to the "add" and "div" functions to examples that can be used with doctest.

* Can you run the tests when the file is loaded as a module?


## Exercise: Convert your script to module
{id: exercise-convert-your-script-to-module}

* Take one of your real scripts (from work or from a previous assignment). Create a backup copy.
* Change the script so it can be import-ed as a module and then it won't automatically execute anything, but that it still works when executed as a script.
* Add a new function to it called `self_test` and in that function add a few test-cases to your code using 'assert'.
* Write another script that will load your real file as a module and will run the `self_test`.
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


## Loaded modules and their path
{id: loaded-modules-and-their-path}

* [sys](https://docs.python.org/library/sys.html)

![](examples/modules/loaded_modules.py)

## Built-in modules
{id: built-in-modules}

![](examples/modules/builtin_modules.py)

