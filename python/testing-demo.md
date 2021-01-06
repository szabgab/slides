# Testing Demo
{id: testing-demo}


## Testing Flask
{id: demo-testing-flask}

* [flask](https://flask.palletsprojects.com/)
* [flask on GitHub](https://github.com/pallets/flask)

```
git clone https://github.com/pallets/flask.git
cd flask
pip install -r requirements/tests.txt
pytest
```


## How do you test your code?
{id: how-do-you-test-your-code}

{aside}
This mini-series is for people who don't have the time to delve into the way you'd write tests for your Python code,
but would like to get a quick overview of the possibilities.

However before we can get into actually testing things, it is worth to think about and even to discuss the following questions.
{/aside}

* What kind of things do you test?

* Web application?
* Command line application?
* Databases?
* ...


## What is testing?
{id: what-is-testing}

{aside}
So what do we really mean when we mean testing?

For every piece of code wether its is a small module or a huge application you can have the following equasion.

There some environment the code works in. It might be just the interpreter/compiler in case of a single stand-alone function,
or it might include multiple networking elements, servers, databases, ioT deviecs etc. No matter what, the environment
is called by the testing people the "Fixture".

Then execute the code - the Application Under Test - and give it some input.

The result should be some "Expected Output".

So this is our equasion.
{/aside}

* Fixture + Input = Expected Output


## What is testing really?
{id: what-is-testing-really}

{aside}
In reality, however, many times we don't get exactly the expected output. Instead there is a small (or big) difference.
That's the bug.

The goal of (automated) testing is to make it easy and cheap to notice when these bugs creep in.

To put it in other words, when you write your code you can check if the result is as expected either manually or by writing
some automated tests. The question, how will you know your piece of code still works half a year from now when someone made
some changes to some other part of the code?

Will you repeate all the manual tests you did earlier? You won't have time for that.

On the other hand if you automated your tests in the first place, then you can easily, quickly and cheaply run them again
and you can verify if everything still works as earlier or if a bug appeared.
{/aside}

* Fixture + Input = Expected Output + Bugs

## Testing demo tools
{id: testing-demo-tools}

{aside}
In these examples we are going to see 3 Python modules that can be used for testing.
{/aside}

* doctest
* unittest
* pytest

## Testing demo methodology
{id: testing-demo-methodology}

{aside}
We won't delve deep into the capabilities of these testing libraries. We will only us a very simple example to
show how to write a passing and a failing test.
{/aside}

* Have a simple AUT - Application Under Test with an obvious bug
* Write a passing test
* Write a failing test


## Testing demo - AUT - Application Under Test
{id: testing-demo-aut}

Given the following module with a single function, how can we use this function and how can
we test it?

![](examples/testing-demo/mymath.py)

{aside}
You probably noticed that our function was called `add` and so the expectation is that it will be able to add two numbers.
However the implementation has a bug. It actually multiplies the two numbers. I know it is a very obvious issue,
but it is great as it allows us to see the mechanics of testing without getting distracted by
a complex implementation and a complex problem.

Rest assured, the mechanism of the testing would be the same even if our function was calculating the moon-landing trajectory.
{/aside}


## Testing demo - use the module
{id: testing-demo-user-the-module}

{aside}
Before we start writing an "automated test", let's see how one could test this code "manually". In reality I see this
many times, that people write short snippets of code to check if their real code works properly, but they
don't turn these small snippets into real tests.

Basically the question is "How can we use the add function of the mymath module?"

The code is straight forward. We import the module. We import the "sys" module to be able to access the command line arguments.
We take two arguments from the command line, call the function, and print the result.

Then, if we would like to make sure our code works well, we can compare that result to some expected result.

Based on this everything works fine.
{/aside}

![](examples/testing-demo/use_mymath.py)

```
python use_mymath.py 2 2
4
```

## Testing demo: doctest
{id: testing-demo-doctest}
{i: doctest}
{i: $?}
{i: %ERRORLEVEL%}

{aside}
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
{/aside}

![](examples/testing-demo/doctest_first/mymath.py)

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

## Testing demo: doctest with failure
{id: testing-demo-doctets-with-failure}

{aside}
Of course we know that our code is not perfect (to say the least) so at one point someone will complain about the
incorrect results received, for example in case they try to add 3 and 3. Before running and fixing the code however
it is better to write a test case with the expected correct result that will fail.

So we added another example to the documentation.

If we run the same command as we did earlier we'll get an extensive output on the screen and the exit code
with have some value different from 0.

At this point you'd probably also go and fix the code, but you have also increased the number of tests and
eliminated the possibility of this failure to return unnoticed.
{/aside}

![](examples/testing-demo/doctest_fail/mymath.py)


![](examples/testing-demo/doctest_fail/mymath.out)

```
$ python -m doctest mymath.py
$ echo $?
1
```

```
> python -m doctest mymath.py
> echo %ERRORLEVEL%
1
```



## Testing demo: Unittest success
{id: testing-demo-unittest}
{i: unittest}
{i: TestCase}
{i: assertEqual}

{aside}
Python comes with a built-in module for writing tests. Its name is `unittest` which might be a bit confusing
as this module can be used to any kind of more complex feature-tests and other modules can be also used to write
so called unit-tests.

Unlike the doctests that were part of the actual code, the unittest library calls for separate test files.
It is recommended that the names of files start with the `test_` prefix as that will make it easy for the various testing
tools to locate them.

Inside the file you'd need to import both the `unittest` module and the module that we are testing. `mystest` in this case.

We need a class with a name that starts with `Test` and inherits from `unittest.TestCase`. In the class we can have one or more
testing functions. Each one starts with a `test_` prefix.
Inside the function we can call the function that we are testing and we can compare the result returned by it to some expected value.
We can compare them in various ways using the various assert-methods of the unittest.TestCase. In this example we used the `assertEqual`
method as we wanted to make sure the actual return value equals the expected value.

We can run the tests using `python -m unittest test_one_with_unittest.py`. It will have some output on the screen indicating all the tests
passed. The exit-code will be 0 as expected.
{/aside}

* [unittest](https://docs.python.org/3/library/unittest.html)

![](examples/testing-demo/test_one_with_unittest.py)


![](examples/testing-demo/test_one_with_unittest.out)

```
$ python -m unittest test_one_with_unittest.py
$ echo $?
0
```

```
> python -m unittest test_one_with_unittest.py
> echo %ERRORLEVEL%
0
```


## Testing demo: Unittest failure
{id: testing-demo-unittest-failure}

{aside}
When we get the report on the incorrect results when adding 3 and 3, we can added another test-case.
We could have added another assertion to the `test_math` function or we could have created a separare
class with its own function, but in this case we opted creating a separate test-function.

We won't go into the pros and contras of each strategy now as we are only interested in the basic technique.

If we run the tests now the output will indicate that it ran 2 test-cases and one of them failed. It even shows
use some details about the expected value and the actual value that can be really useful understanding the
source of the problem.

Note there is also `.F` in the output. The dot indicates the test-function that passed, the F indicates
the test-function that failed.

The exit code is again different from 0.

BTW this exit-code is used by the various CI systems to understand the results of the tests.
{/aside}

![](examples/testing-demo/test_with_unittest.py)

![](examples/testing-demo/test_with_unittest.out)

```
$ python -m unittest test_with_unittest.py
$ echo $?
1
```

```
> python -m unittest test_with_unittest.py
> echo %ERRORLEVEL%
1
```

## Testing demo: pytest using classes
{id: testing-demo-pytest-class}
{i: pytest}
{i: assert}

{aside}
In our third example we are going to use the `pytest` module. The only drawback of the pytest module is that it does not
come with the installation of Python itself. It is not a huge issue though as you probably install hundreds of other
modules as well.

These days Pytest seems like the most popular testing library for Python.

We'll have several examples using Pytest.

In order to use it you'd create a file with a name that starts with `test_` prefix. We need to import the module we are testing
but we don't need to import pytest. Actually we don't even use pytest inside the code. (At least not in the simple use-cases.)
In the file you need to create a class starting with `Test`, but this class does not need to inherit from any special class.
In the class we can have one or more test-functions starting with the prefix `test_`.
In the function we call the function we are testing and we compare the results to the expected results.

We use the built-in `assert` function of Python to check if the results were true.

No need to learn various specialized assert-statements as we had in the `unittest` module.

We run the test using the `pytest` command.

We'll get some output. Here too the single dot after the name of the test file indicates that there was one successful test function.

The exit-code of this execution in 0 as was the case with unittest.
{/aside}


![](examples/testing-demo/test_with_pytest_class.py)

![](examples/testing-demo/test_with_pytest_class.out)

```
$ pytest test_with_pytest_class.py
$ echo $?
0
```

```
> pytest test_with_pytest_class.py
> echo %ERRORLEVEL%
0
```

## Testing demo: pytest using classes - failure
{id: testing-demo-pytest-class-failure}

{aside}
Here too we can add additional test-functions to the same test-class.
Executing `pytest` will print `.F` indicating one passing test-function and one failing test function.
We'll get detailed explanation where the failure happened.

The exit-code will be different from 0 helping the CI systems and any other external system
to know that the tests have failed.
{/aside}

![](examples/testing-demo/test_with_pytest_class_failure.py)

![](examples/testing-demo/test_with_pytest_class_failure.out)

```
$ pytest test_with_pytest_class_failure.py
$ echo $?
1
```

```
> pytest test_with_pytest_class_failure.py
> echo %ERRORLEVEL%
1
```


## Testing demo: pytest without classes
{id: testing-demo-pytest}

{aside}
In the previous example we used a test-class to write our tests, but in reality in many cases
we don't need the classes. We could just as well write plain test-functions as in this example.

Test-functions without a class around them are easier to write and understand and they are a lot
simplert to graps. So unless you really need the features a class can provide I'd recommend you use
functions only. After all our test code should be a lot more simple than our application code.
{/aside}

![](examples/testing-demo/test_with_pytest.py)

![](examples/testing-demo/test_with_pytest.out)

```
$ pytest test_with_pytest.py
$ echo $?
1
```

```
> pytest test_with_pytest.py
> echo %ERRORLEVEL%
1
```

## Testing demo: pytest run doctests
{id: testing-demo-pytest-run-doctests}

{aside}
The nice thing about `pytest` that it can also run all the doctests in your module.
So you can start your testing journey with doctest and later switch to pytest.

You can easily test your examples in your documentation.
{/aside}

```
$ pytest --doctest-modules mymath.py
```

## Testing demo: pytest run unittest
{id: testing-demo-pytest-run-unittests}

{aside}
Pytest can also run the unit-test. You don't even need to tell it anything special.
It will introspect the test code and if it notices tests-classes that are based on unittest
it will execute them using the unittest module.
{/aside}

```
$ pytest test_one_with_unittest.py
$ pytest test_with_unittest.py
```

## Exercise: Testing demo - anagrams
{id: exercise-testing-demo}

* An [anagram](https://en.wikipedia.org/wiki/Anagram) is a pair of words that are created from exactly the same set of characters, but of different order.
* For example **listen** and **silent**
* Or **bad credit** and **debit card**
* Given the following module with the **is_anagram** function write tests for it. (in a file called test_anagram.py)
* Write a failing test as well.
* Try **doctest**, **unittest**, and **pytest** as well.

![](examples/testing-demo/anagram.py)


Sample code to use the Anagram module.


![](examples/testing-demo/use_anagram.py)

## Exercise: Test previous solutions
{id: exercise-test-previous-solutions}

* Go back to your solutions to the previous exercises
* Write tests
* If you feel it is hard, maybe you need to change the code to make it more testable.



## Solution: Testing demo
{id: solution-testing-demo}
![](examples/testing-demo/test_solution_anagram.py)




