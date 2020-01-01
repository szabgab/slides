# Testing Demo
{id: testing-demo}

## How do you test your code?
{id: how-do-you-test-your-code}

* What kind of things do you test?



## What is testing?
{id: what-is-testing}

* Fixture + Input = Expected Output



## What is testing really?
{id: what-is-testing-really}

* Fixture + Input = Expected Output + Bugs



## Testing demo - AUT - Application Under Test
{id: testing-demo-aut}
![](examples/testing-demo/mymath.py)


## Testing demo - use the module
{id: testing-demo-user-the-module}
![](examples/testing-demo/use_mymath.py)


## Testing demo: doctets
{id: testing-demo-doctes}

![](examples/testing-demo/mymath_doctest_first.py)

```
python -m doctest mymath_doctest_first.py
echo $?
0
```

![](examples/testing-demo/mymath_doctest.py)

```
python -m doctest mymath_doctest.py
```
![](examples/testing-demo/mymath_doctest.out)


## Testing demo: Unittest
{id: testing-demo-unittest}
![](examples/testing-demo/test_with_unittest.py)

```
python -m unittest test_with_unittest.py
```
![](examples/testing-demo/test_with_unittest.out)


## Testing demo: pytest using classes
{id: testing-demo-pytest-class}
![](examples/testing-demo/test_with_pytest_class.py)

```
pytest test_with_pytest_class.py
```
![](examples/testing-demo/test_with_pytest_class.out)


## Testing demo: pytest
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




