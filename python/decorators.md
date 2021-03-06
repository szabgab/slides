# Decorators
{id: decorators}

## Decorators: simple example
{id: decorators-example}

* A decorators is that @something just before the declaration of the function.
* Decorators can modify the behavior of functions or can set some meta information about them.

![](examples/decorators/simple.py)

## Decorators - Flask
{id: decorators-flask}

* In Flask we use decorators to designate function as "routes".

![](examples/decorators/flask_app.py)

```
FLASK_APP=flask_app flask run
```

## Decorators - Pytest
{id: decorators-pytest}

* In Pytest we can use decorators to add special marks to test functions
* ... or to mark them as fixtures.

![](examples/decorators/test_with_decorator.py)

```
pytest -v
```
## Decorators caching - no cache
{id: decorators-caching-no-cache}

* Each call will execute the function and do the (expensive) computation.

![](examples/decorators/no_cache.py)
![](examples/decorators/no_cache.out)

## Decorators caching - with cache
{id: decorators-caching-with-cache}
{i: cache}
{i: lru_cache}

* By adding the lru_cache decorator we can tell Python to cache the result and save on computation time.
* [functools](https://docs.python.org/3/library/functools.html)

![](examples/decorators/with_lru_cache.py)
![](examples/decorators/with_lru_cache.out)

## LRU - Least recently used cache
{id: decorators-lru-cache-1}

* [LRU - Cache replacement policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)
* When we call the function with (1, 5) it removes the least recently used results of (1, 2)
* So next time it has to be computed again.

![](examples/decorators/lru_cache_example_1.py)

## LRU - Least recently used cache
{id: decorators-lru-cache-2}

* Here we called (1, 2) after (1, 4) when it was still in the cache
* When we called (1, 5) it removed the LRU pair, but it was NOT the (1, 2) pair
* So it was in the cache even after the (1, 5) call.

![](examples/decorators/lru_cache_example_2.py)

## OOP - classmethod - staticmethod
{id: decorators-classmethod-staticmethod}

![](examples/decorators/myclass.py)
![](examples/decorators/myclass.out)


## Use cases for decorators in Python
{id: decorators-use-cases}
{i: classmethod}
{i: staticmethod}
{i: pytest}

* Common decorators are [@classmethod](https://docs.python.org/3/library/functions.html#classmethod) and  [@staticmethod](https://docs.python.org/3/library/functions.html#staticmethod).
* [Flask](https://flask.palletsprojects.com/) uses them to mark and configure the routes.
* [Pytest](https://docs.pytest.org/) uses them to add marks to the tests.

* [functools](https://docs.python.org/library/functools.html)

* [dataclasses](https://docs.python.org/library/dataclasses.html)
* Logging calls with parameters.
* Logging elapsed time of calls.
* Access control in Django or other web frameworks. (e.g. login required)
* Memoization (caching)
* Retry
* Function timeout
* Locking for thread safety
* [Decorator Library](https://wiki.python.org/moin/PythonDecoratorLibrary)

## Function assignment
{id: function-assignment}

{aside}
Before we learn about decorators let's remember that we can assign function names
to other names and then use the new name:
{/aside}

![](examples/decorators/function_assignment.py)
![](examples/decorators/function_assignment.out)


## Function assignment - alias print to say
{id: function-assignment-alias-print-to-say}

![](examples/decorators/assign_print.py)

## Function assignment - don't do this
{id: function-assignment-dont-do-this}

![](examples/decorators/assign_to_sum.py)

## Passing functions as parameters
{id: passing-functions-as-parameter}

![](examples/decorators/passing_function.py)

## Traversing directory tree
{id: traversing-directory-tree}

![](examples/decorators/tree.py)

## Declaring Functions inside other function
{id: function-inside-other-function}

{aside}
Let's also remember that we can define a function inside another function
and then the internally defined function only exists in the scope of the function
where it was defined in. Not outside.
{/aside}

![](examples/decorators/function_in_function.py)
![](examples/decorators/function_in_function.out)


## Returning a new function from a function
{id: returning-a-function}

![](examples/decorators/return_function.py)
![](examples/decorators/return_function.out)

## Returning a closure
{id: returning-a-closure}

![](examples/decorators/incrementer.py)


## Decorator
{id: decorator}
{i: @}

* A function that changes the behaviour of other functions.
* The input of a decorator is a function.
* The returned value of a decorator is a modified version of the same function.


```
from some_module import some_decorator

@some_decorator
def f(...):
    ...
```

```
def f(...):
    ...
```

```
f = some_decorator(f)
```

## Decorator Demo
{id: decorator-demo}

* Just a simple example created step-by-step

![](examples/decorators/demo.py)

## Decorator to register function
{id: decorator-to-register-function}

* Pytest, Flask probably do this

![](examples/decorators/register.py)

## A recursive Fibonacci
{id: fibo}

![](examples/decorators/fibo.py)


## trace fibo
{id: trace-fibo}

![](examples/decorators/fibotron.py)
![](examples/decorators/fibotron.out)


## tron decorator
{id: decor-tron}

![](examples/decorators/decor.py)


## Decorate with direct call
{id: trace-fibo-direct}

![](examples/decorators/fibotron_direct.py)


## Decorate with parameter
{id: trace-fibo-with-parameter}

![](examples/decorators/fibotron_param.py)
![](examples/decorators/fibotron_param.out)


## Decorator accepting parameter
{id: decor-tron-with-parameter}
![](examples/decorators/decor_param.py)


## Decorate function with any signature
{id: decorate-function-with-any-signature}

* How can we decorate a function that is flexible on the number of arguments?
* Accept `*args` and `**kwargs` and pass them on.

![](examples/decorators/any_func.py)

## Decorate function with any signature - implementation
{id: decorate-function-with-any-signature-implementation}

![](examples/decorators/decor_any.py)
![](examples/decorators/any_func.out)


## Decorate function with any signature - skeleton
{id: decorate-function-with-any-signature-skeleton}

![](examples/decorators/decor_any_skeleton.py)
![](examples/decorators/decor_any_skeleton.out)

## Decorate function with any signature - skeleton with name
{id: decorate-function-with-any-signature-skeleton-with-name}

![](examples/decorators/decor_any_skeleton_with_name.py)
![](examples/decorators/decor_any_skeleton_with_name.out)


## Functool - partial
{id: functool-partial}
{i: partial}

![](examples/decorators/partial.py)



## Exercise: Logger decorator
{id: exercise-logger-decorator}

* In the previous pages we created a decorator that can decorate arbitrary function logging the call and its parameters.
* Add time measurement to each call to see how long each function took.


## Exercise: decorators decorator
{id: exercise-decorators}


Write a function that gets a functions as attribute and returns a new functions while memoizing (caching) the input/output pairs.
Then write a unit test that checks it.
You probably will need to create a subroutine to be decoratorsd.


* Write tests for the fibonacci functions.
* Implement the decorators decorator for a function with a single parameter.
* Apply the decorator.
* Run the tests again.
* Check the speed differences.
* or decorate with tron to see the calls...


## Solution: Logger decorator
{id: solution-logger-decorator}

![](examples/advanced/logger_decor.py)


## Solution: Logger decorator (testing)
{id: solution-logger-decor-testing}

![](examples/advanced/varargs_decor.py)
![](examples/advanced/varargs_decor.out)


## Solution decorators decorator
{id: solution-decorators}

![](examples/decorators/fibonacci.py)
![](examples/decorators/memoize_nonlocal.py)
![](examples/decorators/memoize_attribute.py)

Before


```
$ time python fibonacci.py 35
9227465

real   0m3.850s
user   0m3.832s
sys    0m0.015s
```

After


```
$ time python fibonacci.py 35
9227465

real   0m0.034s
user   0m0.019s
sys    0m0.014s
```
## A list of functions
{id: list-of-dunctions}

![](examples/decorators/functions_in_list.py)
![](examples/decorators/functions_in_list.out)


