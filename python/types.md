# Types in Python
{id: types}

## mypy
{id: mypy}
{i: mypy}

* [mypy](http://mypy-lang.org/)
* [Type Checking](https://realpython.com/python-type-checking/)
* [type hints](https://docs.python.org/library/typing.html)

```
pip install mypy
```

## Changing types
{id: changing-types}

{aside}
Even without any additional work, running mypy on an existing code-base can reveal locations that might need fixing.

For example it can point out places where the content of a variable changes type. Python accepts this, and in some places
this type of flexibility might have advantages, but it can also lead to confusion for the maintainer of this code.
{/aside}

![](examples/types/simple.py)

`python simple.py` works without complaining.

`mypy simple.py` reports the following:

![](examples/types/simple.out)

## Changing types when reading a number
{id: changing-types-when-reading-a-number}

{aside}
A quite common case in the real-world when you read in something that is supposed to be a number.
In terms of the Python type-system the input is always a string. Even if it looks like a number.
We then need to convert it to int() or to float() to use them as such.

People will often reuse the same variable to first hold the string and then the number. This is ok with Python,
but might be confusingt to the reader.
{/aside}

![](examples/types/input.py)

`mypy input.py` will print the following:

![](examples/types/input.out)

## Types of variables
{id: types-of-variables}

![](examples/types/variables.py)

`python variables.py`

![](examples/types/variables.out)

`mypy variables.py`

![](examples/types/variables.mypy)

## Types of function parameters
{id: types-of-function-parameters}

![](examples/types/function.py)
![](examples/types/function.out)
![](examples/types/function.mypy)


## Types function returns None or bool
{id: mypy-to-check-function-returns}

{aside}
-> bool means the function returns a boolean. Either True or False.

-> None means the function returns None. Explicitely, or implicitely.
{/aside}

![](examples/types/function_bool.py)
![](examples/types/function_bool.out)

## Types used properly
{id: types-used-properly}


![](examples/types/good.py)
![](examples/types/good.out)
![](examples/types/good.mypy)

## TODO: mypy
{id: mypy-todo}

* Complex data structures?
* My types/classes?
* Allow None (or not) for a variable.
