# Advanced Exception handling
{id: python-advanced-exceptions}

## Exceptions else
{id: exceptions-else}
{i: else}

* The else part will be execute after each successful "try". (So when there was no exception.)

![](examples/exceptions/else.py)
![](examples/exceptions/else.out)


## Exceptions finally
{id: exceptions-finally}
{i: finally}

* We can add a "finally" section to the end of the "try" - "except" construct.
* The code in this block will be executed after **every** time we enter the **try**.
* When we finish it successfully. When we catch an exception. (In this case a ZeroDivisionError exception in file zero.txt)
* Even when we don't catch an exception. Before the exception propagates up in the call stack, we still see the "finally" section executed.

![](examples/exceptions/finally.py)
![](examples/exceptions/finally.out)


## Exit and finally
{id: exit-finally}
{i: finally}

{aside}
The "finally" part will be called even if we call "return" or "exit" in the "try" block.
{/aside}

![](examples/exceptions/exit_finally.py)


## Catching exceptions
{id: try-except}
{i: try}
{i: except}
{i: finally}

![](examples/advanced/try.py)
![](examples/advanced/try.out)


## Home made exception
{id: home-made-exception}

{aside}
You can create your own exception classes that will allow the user to know what kind of an exception was caught or to capture only the exceptions of that type.
{/aside}

![](examples/exceptions/home_made_exception.py)
![](examples/exceptions/home_made_exception.out)


## Home made exception with attributes
{id: raise-home-made-exception}

![](examples/exceptions/raise_home_made_exception.py)


## Home made exception hierarcy
{id: home-made-exception-hierarchy}

![](examples/exceptions/colors.py)


## Home made exception hierarcy - 1
{id: home-made-exception-hierarchy-1}

![](examples/exceptions/hierarchy1.py)
![](examples/exceptions/hierarchy1.out)


## Home made exception hierarcy - 2
{id: home-made-exception-hierarchy-2}

![](examples/exceptions/hierarchy2.py)
![](examples/exceptions/hierarchy2.out)


## Home made exception hierarcy - 3
{id: home-made-exception-hierarchy-3}

![](examples/exceptions/hierarchy3.py)
![](examples/exceptions/hierarchy3.out)


## Exercise: spacefight with exceptions
{id: exercise-exceptions}

Take the number guessing game (or one-dimensional space-fight) and add exceptions
for cases when the guess is out of space (0-200 by default), or when the guess is not
a number.

![](examples/advanced/spacefight.py)


## Exercies: Raise My Exception
{id: exercise-exception-raise-my-exception}

This is very similar to the exercise the first chapter about exceptions, but
in this case you need to create your own hierarchy of exception classes.

* Write a function that expects a positive integer as its single parameter.
* Raise exception if the parameter is not a number.
* Raise a different exception if the parameter is not positive.
* Raise a different exception if the parameter is not whole number.
* In each case make sure both the text and the type of the exceptions are different.
* Include the actual value received as an attribute in the exception object.


## Solution: spacefight with exceptions
{id: solution-exceptions}

![](examples/advanced/spacefight_exceptions.py)
![](examples/advanced/spacefight_exceptions.out)


## Solution: Raise My Exception
{id: solution-exception-raise-my-exception}

![](examples/exceptions/my_positive.py)
