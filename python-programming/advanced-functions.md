# Advancted functions
{id: advanced-functions}

## Variable scopes
{id: variable-scopes}

* Local (inside a def)
* Enclosing (in the enclosing def, aka. nonlocal)
* Global (outside of all defs)



## Name resolution order (LEGB)
{id: name-resolution-order}

1. Local
1. Enclosing
1. Global
1. Built-in



## Scoping: global seen from fuction
{id: scoping-global-seen-from-function}
![](examples/advanced/scoping_local_variable.py)

42



## Assignment creates local scope
{id: scoping-assignment-creates-local-scope}
![](examples/advanced/scoping_external_variable_fixed.py)
![](examples/advanced/scoping_external_variable_fixed.out)


## Local scope gone wrong
{id: local-scope-gone-wrong}
![](examples/advanced/scoping_external_variable.py)
![](examples/advanced/scoping_external_variable.err)


Accessing a global variable inside a function works, but if I change it (make it refer to another piece of data),
then it is disallowed. If I only change the data inside (for mutable variables), that works, but is a bad practice.




## Changing global variable from a function
{id: changing-global-variable}
![](examples/advanced/global_variable.py)

Does not need to be created outside

![](examples/advanced/global_variable_in_def.py)


## Global variables mutable in functions
{id: mutable-in-function}
![](examples/advanced/mutable_in_def.py)


## Scoping issues
{id: scoping-issues}
![](examples/advanced/scoping_issues.py)

List comprehensions don't create their own scope!



## sub in sub
{id: sub-in-sub}

Functions can be defined inside functions.

![](examples/advanced/sub_in_sub.py)

They are scoped locally




## Scoping sub in sub (enclosing scope)
{id: scoping-internal-sub}
![](examples/advanced/scoping_internal_sub.py)
![](examples/advanced/scoping_internal_sub.out)


## Function objects
{id: function-objects}

```
The difference between
x = foo
y = foo()
```
![](examples/advanced/function-objects.py)


## Functions are created at run time
{id: runtime-def}

{aside}

def and class are run-time
Everything is runtime. Even compilation is runtime.

foo() will return a random value every time, but when
bar is defined it freezes the specific value that foo
returned when bar was created.
{/aside}
![](examples/advanced/runtime-def.py)
![](examples/advanced/runtime-def.out)


## Mutable default
{id: function-parameters-mutable-default}


The default list assigned to b is created when the f functions is defined.
After that, each call to f() (that does not get a "b" parameter) uses this
common list.


![](examples/advanced/mutable_default_parameter.py)
![](examples/advanced/mutable_default_parameter.out)

Use None instead:



## Use None as default parameter
{id: none-as-default-parameter}
![](examples/advanced/none_as_default_parameter.py)
![](examples/advanced/none_as_default_parameter.out)


## Inner function created every time the outer function runs
{id: runtime-inner-def}

{aside}

Also defined during run-time, but in every call of bar() the innter_func is redefined
again and again.
{/aside}
![](examples/advanced/runtime-inner-def.py)
![](examples/advanced/runtime-inner-def.out)


## Static variable
{id: static-variable}
{i: static}

There are no function-level static variables in Python, but you can fake it quite easily

![](examples/advanced/static.py)


## Static variable in generated function
{id: static-variable-in-generated-func}
![](examples/advanced/generated_static.py)



## Inspect
{id: inspect}


The [inspect](http://docs.python.org/library/inspect.html) module provides introspection to Python runtime.
<emp>inspect.stack</emp> returns the stack-trace. Element 0 is the deepes (where we called inspect stack).
Each level has several values. A represantation of the frame, filename, linenumber, subroutine-name.


![](examples/advanced/caller.py)


python caller.py 1


![](examples/advanced/caller_1.out)


