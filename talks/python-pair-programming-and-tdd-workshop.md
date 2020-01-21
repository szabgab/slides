# Pair Programming and TDD
{id: python-pair-programming-and-tdd}

## Slides
{id: slides}

* [slides](https://code-maven.com/slides/python-pair-programming-and-tdd-workshop/)



## Parts of the session
{id: parts-of-the-session}

* Introduction to Testing in Python. (10 min)
* Pair programming a project using TDD.(80 min)
* Switching pairs to explain the solution to each other. (30 min)
* Retrospective. (30 min)



## Goals
{id: goals}

* Improve our way of software development.
* Experiment with TDD.
* Experiment with Pair Programming.



## Module to test
{id: module-to-test}
![](python-pair-programming-and-tdd-workshop/test/mymath.py)


## Test the module
{id: test-mymath}
![](python-pair-programming-and-tdd-workshop/test/test_mymath.py)


## Running Pytest
{id: running-pytest}

```
pytest test_mymath.py
```
![](python-pair-programming-and-tdd-workshop/test/test_mymath.txt)


## Test the module even more
{id: test-mymath-more}
![](python-pair-programming-and-tdd-workshop/test/test_mymath_more.py)


## Running Pytest
{id: running-pytest-again}

```
pytest test_mymath_more.py
```
![](python-pair-programming-and-tdd-workshop/test/test_mymath_more.txt)


## Pytest Coverage
{id: pytest-coverage}

```
pip install pytest-cov
pytest --cov=my --cov-report html --cov-branch
Open htmlcov/index.html
```


## Learning Pytest
{id: learning-pytest}

* [Testing with Pytest](https://code-maven.com/slides/python-programming/testing-with-pytest)
* [pytest.org](http://pytest.org)
* [Python Testing by Brian Okken](http://pythontesting.net/)



## TDD - Test Driven Development
{id: test-driven-development}

* Write test first. It fails.
* Implement code. Test passes.
* Run test with coverage and check if there are cases that you have not covered yet.
* Git commit



## Why in pairs?
{id: why-in-pairs}

* Learn from each other.
* Learn how to express our ideas.
* Continuous peer review.
* Better solutions.
* Less bugs.
* You already know how to program alone. Let's try something else now.



## Pair Programming
{id: pair-programming}

* There is no single right way to do it. Experiment!
* Verbalize everything
* Driver - Navigator
* Driver - Navigator - Observer



## Llewellyn's Strong Style Pairing
{id: strong-style-pairing}

* "For an idea to go from your head into the computer it MUST go through someone else's hands."
* [Llewellyn's strong-style pairing](http://llewellynfalco.blogspot.com/2014/06/llewellyns-strong-style-pairing.html)



## Llewellyn's Strong Style Pairing: Driver
{id: strong-style-pairing-driver}

* "Trust your navigator"
* "Become comfortable working with incomplete understanding"
* "What if I have an idea I want to implement?" - switch!



## Llewellyn's Strong Style Pairing: Navigator
{id: strong-style-pairing-navigator}

* "Give the next instruction to the driver the instant they are ready to implement it."
* "Talk in the highest level of abstraction the driver can understand."



## Tic-tac-toe
{id: tic-tac-toe}

* [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe)

![](tic-tac-toe.png)


## Tic-tac-toe - hints
{id: tic-tac-toe-hints}

* Decide on a representation of the board.
* Allow the computer to recognize when someone won.
* Report invalid boards?
* Allow two humans to play.
* Make the computer play.
* Make the system play against itself.
* Watch [War Games](https://en.wikipedia.org/wiki/WarGames).



## Retrospective
{id: retrospective}



