# Mocking Python
{id: index}

## Plan
{id: plan}

* Introducton
* Presentation about Mocking
* Hands-on exercises
* Retrospective
* Job searching help

## About me
{id: about-me}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* Help tech teams move faster with more stability and more predictability.
* [PyWeb](https://www.meetup.com/PyWeb-IL/)
* [Code Maven workshops](https://www.meetup.com/Code-Mavens/)

## Goal
{id: goal}

You will come out from the workshop knowing

* What is Mocking and Monkey Patching?
* When to use it?
* What are the dangers?

* Experiment with mocking in various situations.


## Fixtures
{id: fixtures}

* Fixtures - the environment in which a test runs (the outside world)
* Directory layout - files
* Database with or without data etc.

## Fixtuers in Pytest
{id: fixtures-in-pytest}

* A more generic term
* Helper tools to run and analyze your test code

## Temporary directory - tmpdir

```
def test_read_ini(tmpdir):
d = tmpdir.mkdir("subdir")
fh = d.join("config.ini")
fh.write("""
""")
```

## Test Doubles
{id: test-doubles}

* Mocks
* Spies
* Stubs
* Fakes
* Dummies

* [Gerard Meszaros - xUnit Test Patterns](https://martinfowler.com/books/meszaros.html)
* [Test Double explained by Martin Fowler](https://martinfowler.com/bliki/TestDouble.html)

## What is Mocking and Monkey Patching?
{id: what-is-mocking-monkey-patching}

* Replace some internal part of a module or class for the sake of testing.
* Mocking
* Monkey Patching

## Situations
{id: situations}

* TDD

* Write application agains API that is not ready yet or not controlled by you.

* Replace a complex object with a simpler one.

* Isolate parts of the system to test them on their own.

* Speed up tests (e.g. eliminate remote calls, eliminate database calls).

* Simulate cases that are hard to replicate. (What if the other system fails?)

* Unit tests.

## Unit testing vs. Integration testing
{id: unit-testing-vs-integration-testing}

![dryer](dryer.mp4)

## Experiment with mocking in various situations

{id: experiment-with-mocking}

* Mocking external calls.
* Mocking method calls.
* Mocking a whole class.
* Mocking time.
* Mocking IO

## Examples are simple
{id: examples-are-simple}

* Don't worry, real life code is much more complex!

## Simple test case using Pytest
{id: simple-test-case}

A simple module with a function:

![](ex1/app.py)

The test:

![](ex1/test_app.py)

Running `pytest`:

```
======================== test session starts ========================
platform darwin -- Python 3.6.3, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: /Users/gabor/work/slides/python-mocking/ex1, inifile:
plugins: cov-2.5.1
collected 1 item

test_app.py .                                                 [100%]

===================== 1 passed in 0.01 seconds ======================
```

## Hard coded path
{id: hard-coded-path}

![](exa/app.py)

![](exa/test_data_1.py)

pytest test_data_1.py

```
    def get_sum():
>       with open(data_file) as fh:
E       FileNotFoundError: [Errno 2] No such file or directory: '/corporate/fixed/path/data.json'
```

## Manually Patching attribute
{id: mocking-attribute}

![](exa/test_data_2.py)

![](exa/test_1.json)

## Monkey Patching attribute
{id: monkeypatching-attribute}

![](exa/test_data_3.py)

## Monkey Patching functions
{id: mocking-functions}

![](exo/aut.py)

![](exo/test_aut_attr.py)

## Monkey Patching dictionary items
{id: mocking-dictionary-item}

![](exb/aut.py)

![](exb/test_aut_item.py)

## Mocking a whole class
{id: mocking-a-whole-class}

![](classy/app.py)

![](classy/data.json)

![](classy/test_app.py)

## Mocking input/output
{id: mocking-input-output}

![](ex2/app.py)

The test:

![](ex2/test_app.py)

## Mocking input/output
{id: manually-mocking-input-output}

![](ex2/test_calc.py)

## Mocking random numbers
{id: mocking-random-numbers}

* Mock the methods of the `random` module

## Exercises
{id: exercise}

[Download zip file](https://github.com/szabgab/slides) or clone repository using

```
git clone https://github.com/szabgab/slides.git
```

the files are in the directory.

```
slides/python-mocking/
```

## Work in pairs
{id: work-in-pairs}

* Navigator - Driver
* Driver - Observer

## Exercise: One Dimentsional space-fight
{id: one-dimensional-space-fight}

* `space-fight` directory.
* Write a test that check the 'x' button works.
* Write a test that check system can properly report 'less than'.
* Write a test that check system can properly report 'greater than'.
* Write a test that check system can properly report 'found'.

* You might need to mock input/output/random.

![](space-fight/game.py)

## Exercise: web client
{id: web-client}

* `crawler` directory.
* Test this application without hitting any web site.
* Test what happens if the URL returns 404
* What if it is a 500 error?
* What if the host not found?

![](crawler/app.py)

## Exercise: Open WeatherMap client
{id: openweather}

* [get API key](https://home.openweathermap.org/api_keys)
* It takes 10 minutes to activate the key, so do it now.
* Once you observerd that the code works, test it without internet access.

**config.ini**

```
[openweathermap]
api=93712604
```

![](weather/get_weather.py)

## Mocking A Bank
{id: mocking-a-bank}

![](exdb/bank.py)

![](exdb/db.py)

## Testing the whole application
{id: testng-the-whole-application}

* Implement the tests without the need for a database.

![](exdb/test_db_app.py)


## Resources
{id: resources}

* [MonkeyPatching](https://docs.pytest.org/en/latest/monkeypatch.html)
* [Python slides](https://code-maven.com/slides/python-programming/)
* [Python testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)

## Retrospective
{id: retrospective}

* What went well?
* What needs improvement?

## Job searching help
{id: job-searching}

* LinkedIn
* Open source projects

## Solutions - game
{id: solutions}

![](tests/test_game_exit.py)

![](tests/test_game_play.py)

## Solutions - Mocking the database access
{id: mocking-database-access}

![](tests/test_db_app_mocking.py)


