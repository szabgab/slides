# Fixtures and Mocking in Python
{id: index}

## How do you test Moon-landing?
{id: test-moon-landing}

* without actually flying to the moon?

## How do you test a system ...
{id: how-do-you-test}

* that sends a verification email?
* that relies on random values?
* in parallel without interference?
* together with a 3rd party?
* when a 3rd party it uses fails?
* with a timeout

## Plan
{id: plan}

* Introducton
* Presentation about Fixtures and Mocking
* Hands-on exercises
* Retrospective
* Job searching help

## About me
{id: about-me}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* Help tech teams move faster with more stability and more predictability.
* Automation
* DevOps
* [Code Maven Workshops](https://workshops.code-maven.com/)
* [Code Maven Workshops on Meetup](https://www.meetup.com/Code-Mavens/)

## Goal
{id: goal}

You will come out from the workshop knowing

* What are Fixtures?
* What is Mocking and Monkey Patching?
* When to use them?
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


## Traditional xUnit fixtures
{id: traditiona-fixtures}

![](traditional/test_fixture.py)

```
$ pytest test_fixture.py -s

setup_module

  setup_function
    test_one
    test_one after
  teardown_function

  setup_function
    test_two
  teardown_function

  setup_function
    test_three
    test_three after
  teardown_function

teardown_module
```


## Dependency Injection
{id: dependency-injection}

* Use introspection to find out what a method needs
* Pass in the right arguments

![](dependency-injection.py)

## Temporary directory - tmpdir
{id: temporary-directory}

* tmpdir

```
def test_something(tmpdir):
    d = tmpdir.mkdir("subdir")
    fh = d.join("config.ini")
    fh.write("""
      Some config
    """)
```

* Directory location: /private/var/folders/ry/z60xxmw0000gn/T/pytest-of-gabor/pytest-14/test_read0
* Directory cleanup

## Capture STDOUT and STDERR - capsys
{id: capsys}

* capsys

![](capture/test_capture.py)


## Home-made fixture
{id: home-made-fixture}

![](fixture_inject/test_app.py)

## Home-made fixture with tempdir
{id: home-made-fixture-tempdir}

![](fixture_inject_tmpdir/test_app.py)

```
$ pytest -qs
{'name': 'Foo Bar', 'email': 'foo@bar.com'}
```

## Home-made fixture with temp directory
{id: home-made-fixture-with-temp-directory}


## Fixture Autouse
{id: fixture-autouse}

* In the test file

![](fixture_autouse/test_app.py)

```
$ pytest -sq
Before
In test
.After

1 passed in 0.02 seconds
```


## conftest.py
{id: conftest}

![](fixture_autouse_conftest/conftest.py)

![](fixture_autouse_conftest/test_app.py)


## Fixture for MongoDB
{id: fixture-for-mongodb}

![](fixture_autouse_db/conftest.py)


## Test Doubles
{id: test-doubles}

* Mocks
* Spies
* Stubs
* Fakes
* Dummies

* [Gerard Meszaros - xUnit Test Patterns](https://martinfowler.com/books/meszaros.html)
* [Test Double explained by Martin Fowler](https://martinfowler.com/bliki/TestDouble.html)


## Test Doubles explained
{id: test-doubles-explained}


Dummy objects are passed around but never actually used.

Fakes - Working implementation, but much simple
* An in-memory list of username/password pairs that provide the authentication)
* A database interface where data stored in memory only, maybe in a dictionary.

Mocks - Mocks are objects that register calls they receive, but do not execute the real system behind.

Stubs - Stub is an object that holds predefined data and uses it to answer calls during tests.
* A list of "random values"
* Responses given to prompt

Spies usually record some information based on how they were called and then call the real method. (or not)

## Verify behavior or state?
{id: verify-behavior-or-state}



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

## Hard coded path
{id: hard-coded-path}

In many application we can find hard-coded pathes. In order to test them we will need to create that exact path
which is not always easy. This also means we cannot run two tests at the same time with different content in those
files. (The actual "application" is just adding numbers together.)

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

We can replace the attribute during the test run and create a json file locally to be used.
At least two problems with this:

* Readers might glance over the assignment and might be baffled
* The change is permanent in the whole test script so one test impacts the other.

![](exa/test_data_2.py)

![](exa/test_1.json)

## Monkey Patching attribute
{id: monkeypatching-attribute}

We can use the monkeypatch fixture to do the same.
* It stands out more as it is a fxture and you can search for the name
* It only applies to the current test function. So they are now independent again.

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

## Exercise: test login expiration
{id: exercise-test-login-expiration}

![](timeout/app.py)

![](timeout/test_app.py)


## Solution: test login expiration
{id: solution-test-login-expiration}

![](timeout/test_timeout.py)

## Exercise: Record e-mail sending
{id: record-email}

Implement a registration for a Flask (or other) web application:
Accept e-mail as input send e-mail with a code to the given address use that code to verify e-mail address.
Without actually sending e-mails.

## Exercise: Fixture database
{id: fixture-database}

Set up a database (can be sqlite, mysql, postgresql, mongodb, etc.) for each test run.


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

## Exercise: Mocking A Bank
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
* [Test Doubles - Fakes, Mocks and Stubs.](https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da)
* [Martin Fowler: Test Double](https://martinfowler.com/bliki/TestDouble.html)

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


