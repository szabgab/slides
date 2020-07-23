# Testing Demo
{id: testing-demo}

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


## Testing demo - AUT - Application Under Test
{id: testing-demo-aut}

Given the following module with a single function, how can we use this function and how can
we test it?

![](examples/testing-demo/mymath.py)


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

## Testing demo: doctets
{id: testing-demo-doctes}
{i: doctest}

{aside}
The first way we look at is using the "doctest" module. It is a very nice tool that allows us to test our code
and to also verify that our documentation is aligned with the code.
In addition to that doctest is a standard module, it comes with every installation of Python so you don't need
to worry about installation.

The big drawback is that it is not really useful for anything complex.

In Python if you add a string immediately after the declaration of the function - so the line after the "def" statement -
that string becomes the documentation of the function.
{/aside}

![](examples/testing-demo/mymath_doctest_first.py)

```
python -m doctest mymath_doctest_first.py
echo $?
0

echo %ERRORLEVEL%
0
```

![](examples/testing-demo/mymath_doctest.py)

```
python -m doctest mymath_doctest.py
echo $?
1
```

![](examples/testing-demo/mymath_doctest.out)

## Testing demo: Unittest success
{id: testing-demo-unittest}

![](examples/testing-demo/test_one_with_unittest.py)

```
python -m unittest test_one_with_unittest.py
echo $?
0
```

![](examples/testing-demo/test_one_with_unittest.out)

## Testing demo: Unittest failure
{id: testing-demo-unittest-failure}

![](examples/testing-demo/test_with_unittest.py)

```
python -m unittest test_with_unittest.py
echo $?
1
```

![](examples/testing-demo/test_with_unittest.out)


## Testing demo: pytest using classes
{id: testing-demo-pytest-class}

![](examples/testing-demo/test_with_pytest_class.py)

```
pytest test_with_pytest_class.py
```

![](examples/testing-demo/test_with_pytest_class.out)


## Testing demo: pytest without classes
{id: testing-demo-pytest}

![](examples/testing-demo/test_with_pytest.py)

```
pytest test_with_pytest.py
```
![](examples/testing-demo/test_with_pytest.out)


## Testing demo: pytest run doctests
{id: testing-demo-pytest-run-doctests}

```
pytest --doctest-modules mymath_doctest_first.py
pytest --doctest-modules mymath_doctest.py
```


## Testing demo: pytest run unittest
{id: testing-demo-pytest-run-unittests}

```
pytest -v test_with_unittest.py
```


## Exercise: Testing demo
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


## Solution: Testing demo
{id: solution-testing-demo}
![](examples/testing-demo/test_solution_anagram.py)




