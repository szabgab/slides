# Appendix
{id: python-appendix}

## print_function
{id: print-in-the-future}
![](examples/future/print.py)


## Dividers (no break or continue)
{id: divider}

We will see how break and continue work, but first let's see a loop to find all the dividers on a number n.

![](examples/strings/no_break_continue.py)
![](examples/strings/no_break_continue.out)



## Lambdas
{id: lambdas}
![](examples/classes/lambdas.py)


## Abstract Class
{id: abstract-class}
{i: abc}
![](examples/classes/abstract.py)


## Remove file
{id: remove-file}
{i: os.remove}
{i: os.unlink}


[os.remove](https://docs.python.org/library/os.html#os.remove) or
[os.unlink](https://docs.python.org/library/os.html#os.unlink)


## Modules: more
{id: modules-more}
{i: sys.modules}
{i: imp.reload}
{i: reload}

* sys.modules to list loaded modules
* imp.reload to reload module (Just reload before 3.3)

![](examples/modules/mod.py)
![](examples/modules/a.py)


## import hooks
{id: import-hooks}
{i: __import__}


## Python resources
{id: python-resources}

* [Central Python site](https://python.org/)
* [Python documentation](https://docs.python.org/)
* [Learning Python the Hard way](http://learnpythonthehardway.org/)
* [Python Weekly](http://pythonweekly.com/)
* [PyCoder's Weekly](http://pycoders.com/)


## Progress bar
{id: progress-bar}
![](examples/other/progress_bar.py)


## from __future__
{id: from-future}

```
from __future__ import print_function
from __future__ import division
```

or


```
from __future__ import print_function, division
```

See also [__future__](http://docs.python.org/library/__future__.html)


{aside}

We cannot import everything that is in __future__, because we don't know what will be in __future__ in the future....
and we don't want to blindly change the behaviour of Python.
{/aside}


## Variable scope
{id: varaible-scope}
{i: scope}

* There are two scopes: outside of all functions and inside of a function.
* The first assignment to a variable defines it.
* Variables that were declared outside all functions can be seen inside, but cannot be changed.
* One can connect the outside name to an inside name using the 'global' keyword.
* if and for blocks don't provide scoping.

![](examples/basics/scope.py)

{aside}

global scope
{/aside}



## scope
{id: scope-of-names}
![](examples/other/scope_before_def.py)
![](examples/other/scope_after_def.py)

{aside}

If we declare a variable outside of all the subroutines,
it does not matter if we do it before the sub declaration,
or after it. In neither case has the global variable any presence
inside the sub.
{/aside}
![](examples/other/scope_inside_def.py)

{aside}

A name declared inside a subroutine is not visible outside.
{/aside}
![](examples/other/scope_global.py)

{aside}

Unless it was marked using the global word.
{/aside}


## type
{id: type}
{i: type}
{i: __name__}
![](examples/other/type.py)


## Look deeper in a list
{id: deeper}
![](examples/lists/string_deeper.py)




