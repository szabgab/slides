# Testing with PyTest
{id: pytest}

## Pytest features
{id: pytest-features}

* Organize and run test per directory (test discovery)
* Run tests by name matching
* Run tests by mark (smoke, integration, db)
* Run tests in parallel with the xdist plugin.
* Create your own fixtures and distribute them.
* Create your own plugins and distribute them.

## Test methods
{id: pytest-test-methods}

* Functional tests

* Unit test
* Integration test
* Acceptance test

* Regression test

* Code quality tests


## Pytest setup
{id: pytest-setup}

**Python 2**

```
virtualenv venv2
source venv2/bin/activate
pip install pytest
```

**Python 3**

```
virtualenv venv3 -p python3
source venv3/bin/activate
pip install pytest
```

**Python 3 Debian/Ubuntu**

```
apt-get install python3-pytest
```

**Python 3 RedHat/Centos**

```
yum install python3-pytest
```

## Pytest - AUT - Application Under Test
{id: pytest-simple-aut}

{aside}
This is a simple "application" and even that has a bug. Later we'll discuss much more complex cases, but for the unedrstanding
of the Pytest testing framework this simple will do.
{/aside}

![](examples/pytest/math/mymath.py)

## How to use the module?
{id: pytest-how-to-use-the-simple-aut}

{aside}
Before we try to test this function let's see how could we use it?

There is nothing special here, I just wanted to show it, because the testing is basically the same.
{/aside}

![](examples/pytest/math/use_mymath.py)
![](examples/pytest/math/use_again_mymath.py)

## Pytest - simple passing test
{id: pytest-simple-passing-test}

{aside}
We don't need much to test such code. Just the following things:
{/aside}

* Filename startes with `test_`
* A function that starts with `test_`
* Call the test function with some parameters and check if the results are as expected.

{aside}
Specifically the `assert` function of Python expects to recived a True (or False) value.
If it is True the code keeps running as if nothing has happened.

If it is False and exception is raised.
{/aside}

![](examples/pytest/math/test_mymath.py)

{aside}
We can run the tests in two different ways. The regular would be to type in `pytest` and the name of the test file.
In some setups this might not work and then we can also run `python -m pytest` and the name of the test file.
{/aside}

```
pytest test_mymath.py
python -m pytest test_mymath.py
```

![](examples/pytest/math/test_mymath.out)

{aside}
The top of the output shows some information about the environment, (version numbers, plugins) then "collected" tells us how many test-cases were found by pytest.
Each test function is one test case.

Then we see the name of the test file and a single dot indicating that there was one test-case and it was successful.

After the test run we could also see the exit code of the program by typing in `echo $?` on Linux or Mac or `echo %ERRORLEVEL%` on Windows.
{/aside}

```
$ echo $?
0
```

```
> echo %ERRORLEVEL%
0
```

## Pytest failing test in one function
{id: pytest-failing-test-in-one-function}

{aside}
Once we had that passing test we might have shared our code just to receive complaints that it does not always work properly. One use might complain that passing in 2 and 3 does not give the expected 5.

So for your investigation the first thing you need to do is to write a test case expecting it to work proving that your code works. So you add a second assertion.
{/aside}

![](examples/pytest/math/test_mymath_more.py)

{aside}
To your surprise the tests fails with the following output:
{/aside}


![](examples/pytest/math/test_mymath_more.out)

{aside}
We see the `collected 1 item` because we still only have one test function.

Then next to the test file we see the letter F indicating that we had a single test failure.

Then we can see the details of the test failure. Among other things we can see the actual value returned by the `add` function
and the expected value.

Knowing that `assert` only receives the True or False values of the comparision, you might wonder how did this happen.
This is part of the magic of pytest. It uses some introspection to see what was in the expression that was passed to `assert` and it can print out the details
helping us see what was the expected value and what was the actual value. This can help understanding the real problem behind the scenes.


You can also check the exit code and it will be something different from 0 indicating that something did not work.
The exit code is used by CI-systems to see which test run were successful and which failed.
{/aside}

```
$ echo $?
1
```

```
> echo %ERRORLEVEL%
1
```

{aside}
One big disadvantage of having two asserts in the same test function is that we don't have clear indication that the first assert was successful.
Moreover if the first assert fails then the second would not be even executed so we would not know what is the status of that case.
{/aside}

## Pytest failing test separated
{id: pytest-failing-test-separated}

{aside}
Instead of putting the two asserts in the same test function we could also put them in separate onese like in this example.
{/aside}

![](examples/pytest/math/test_mymath_more_separate.py)

{aside}
The result of running this test file shows that it `collected 2 items` as there were two test functions.

Then next to the test file we see a dot indicating the successful test case and an F indicating the failed test. The more detailed test report helps.

At the bottom of the report you can also see that now it indicates 1 failed and 1 passed test.
{/aside}

![](examples/pytest/math/test_mymath_more_separate.out)

## Pytest run all the test files
{id: pytest-run-all-the-test-files}

* in the math directory run `pytest` and let it find all the test files and all the test functions.

```
pytest
```

## Exercise: test simple module
{id: exercise-test-simple-module}

* Take the standard [math](https://docs.python.org/library/math.html) library and write tests for some of the functions.

## Pytest expected exception
{id: pytest-expected-exception}

* What if raising an exception is part of the specification of a function?
* That given certain (incorrect) input it will raise a certain exception?
* How can we test that we get the right exception. The expected exception?

## Pytest a nice Fibonacci example
{id: pytest-fibonacci}

{aside}
This is a nice implementation of the Fibonacci function. If we look at the way we can use it we see that it works well for 10.
{/aside}

![](examples/pytest/fib1/fibonacci.py)
![](examples/pytest/fib1/use_fib.py)
![](examples/pytest/fib1/use_fib.out)

## Pytest  testing Fibonacci
{id: pytest-testing-fibonacci}

![](examples/pytest/fib1/test_fibonacci.py)
![](examples/pytest/fib1/test_fibonacci.out)

* What if the user calls it with -3 ?  We get the result to be 1. We don't want that.

## Pytest expected exception
{id: pytest-expected-exception-2}


![](examples/pytest/fib2/fibonacci.py)
![](examples/pytest/fib2/use_fib.py)
![](examples/pytest/fib2/use_fib.out)

## Pytest testing expected exception
{id: pytest-testing-expected-exception}

![](examples/pytest/fib2/test_fibonacci.py)
![](examples/pytest/fib2/test_fibonacci.out)

## Pytest Change the text of the exception
{id: pytest-change-text-of-exception}

![](examples/pytest/fib3/fibonacci.py)

![](examples/pytest/fib3/test_fibonacci.py)
![](examples/pytest/fib3/test_fibonacci.out)


## Pytest Missing exception
{id: pytest-missing-exception}

![](examples/pytest/fib4/fibonacci.py)
![](examples/pytest/fib4/test_fibonacci.py)
![](examples/pytest/fib4/test_fibonacci.out)

## Pytest Other exception is raised
{id: pytest-other-exception-raised}

![](examples/pytest/fib5/fibonacci.py)
![](examples/pytest/fib5/test_fibonacci.py)
![](examples/pytest/fib5/test_fibonacci.out)

## Pytest No exception is raised
{id: pytest-no-exception-raised}

![](examples/pytest/fib6/fibonacci.py)
![](examples/pytest/fib6/test_fibonacci.py)
![](examples/pytest/fib6/test_fibonacci.out)

## Exercise: test more exceptions
{id: exercise-test-more-exception}

* Find another case that will break the code.
* Then make changes to the code that it will no break.
* The write a test to verify it.

## Solution: test more exceptions
{id: solution-test-more-exception}

![](examples/pytest/fib7/fibonacci.py)
![](examples/pytest/fib7/test_fibonacci.py)
![](examples/pytest/fib7/test_fibonacci.out)


## PyTest: Multiple Failures
{id: pytest-multiple-failures}


![](examples/pytest/test_failures.py)


## PyTest: Multiple Failures output
{id: pytest-multiple-failures-output}

```
test_failures.py .F.F.
```

```
$ pytest -v test_failures.py

test_failures.py::test_one PASSED
test_failures.py::test_two FAILED
test_failures.py::test_three PASSED
test_failures.py::test_four FAILED
test_failures.py::test_five PASSED
```

```
$ pytest -s test_failures.py

one
three
five
```


## PyTest Selective running of test functions
{id: pytest-selective-running-of-test-functions}

```
pytest test_failures.py::test_one

pytest test_failures.py::test_two
```


## PyTest: stop on first failure
{id: pytest-stop-on-first-failure}
{i: --maxfail}
{i: -x}

```
pytest -x
pytest --maxfail 42
```


## Pytest: expect a test to fail (xfail or TODO tests)
{id: pytest-expect-a-test-to-fail}
{i: xfail}


Use the `@pytest.mark.xfail` decorator to mark the test.


![](examples/pytest/test_mymod_3.py)


## Pytest: expect a test to fail (xfail or TODO tests)
{id: pytest-expect-a-test-to-fail-output}

```
$ pytest test_mymod_3.py
```

```
======= test session starts =======
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
Using --random-order-bucket=module
Using --random-order-seed=557111

rootdir: /Users/gabor/work/training/python/examples/pytest, inifile:
plugins: xdist-1.16.0, random-order-0.5.4
collected 2 items

test_mymod_3.py .x

===== 1 passed, 1 xfailed in 0.08 seconds =====
```


## PyTest: show xfailed tests with -rx
{id: pytest-show-xfailed-test}
{i: -rx}

```
$ pytest -rx test_mymod_3.py
```

```
======= test session starts =======
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
Using --random-order-bucket=module
Using --random-order-seed=557111

rootdir: /Users/gabor/work/training/python/examples/pytest, inifile:
plugins: xdist-1.16.0, random-order-0.5.4
collected 2 items

test_mymod_3.py .x

===== short test summary info =====
XFAIL test_mymod_3.py::test_multiword_anagram
  Bug #42

===== 1 passed, 1 xfailed in 0.08 seconds =====
```



## Pytest: skipping tests
{id: pytest-skiping-test}
![](examples/pytest/test_on_condition.py)

```
pytest test_on_condition.py
```

```
collected 4 items

test_on_condition.py ss.s

==== 1 passed, 3 skipped in 0.02 seconds ====
```


## Pytest: show skipped tests with -rs
{id: pytest-show-skipped-tests}
{i: -rs}

```
$ pytest -rs test_on_condition.py
```

```
collected 4 items

test_on_condition.py s.ss

===== short test summary info =====
SKIP [1] test_on_condition.py:15: To show we can skip tests without any condition.
SKIP [1] test_on_condition.py:7: Linux tests
SKIP [1] test_on_condition.py:11: Windows tests

==== 1 passed, 3 skipped in 0.03 seconds ====
```


## Pytest: show extra test summmary info with -r
{id: pytest-show-extra-test-summary-info}
{i: -r}
{i: -ra}

* (f)ailed
* (E)error
* (s)skipped
* (x)failed
* (X)passed
* (p)passed
* (P)passed with output
* (a)all except pP


```
pytest -rx  - xfail, expected to fail
pytest -rs  - skipped
pytest -ra  - all the special cases
```

![](examples/pytest/test_r.py)

```
pytest -h
```

## Pytest: skipping tests output in verbose mode
{id: pytest-skiping-test-output}

```
$ pytest -v test_on_condition.py

test_on_condition.py::test_mac PASSED
test_on_condition.py::test_any SKIPPED
test_on_condition.py::test_windows SKIPPED
test_on_condition.py::test_linux SKIPPED

==== 1 passed, 3 skipped in 0.01 seconds ======
```


## Pytest verbose mode
{id: pytest-verbose}
{i: -v}

```
$ pytest -v test_mymod_1.py

test_mymod_1.py::test_anagram PASSED
```


```
$ pytest -v test_mymod_2.py

test_mymod_2.py::test_anagram PASSED
test_mymod_2.py::test_multiword_anagram FAILED
```


## Pytest quiet mode
{id: pytest-quiet}
{i: -q}

```
$ pytest -q test_mymod_1.py
.
1 passed in 0.01 seconds
```


```
$ pytest -q test_mymod_2.py

.F
=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
1 failed, 1 passed in 0.09 seconds
```


## PyTest print STDOUT and STDERR using -s
{id: pytest-print-stdout-and-stderr}
{i: -s}
{i: -q}
![](examples/pytest/test_stdout_stderr.py)

```
$ pytest -s -q test_stdout_stderr.py
hello testing
stderr during testing
.
1 passed in 0.01 seconds
```


## Exercise: test math functions
{id: pytest-exercise-math}

* Test methods of the [math](https://docs.python.org/3/library/math.html) module.
* ceil
* factorial
* gcd




## Exercise: test this app
{id: pytest-exercise-app}


Write tests for the `swap` and `average` functions of the `app` module. Can you find a bug?


![](examples/pytest/app.py)


## Exercise: test the csv module
{id: pytest-exercise-csv}

* [csv](https://docs.python.org/3/library/csv.html)
* Create a CSV file, read it and check if the results are as expected!
* Test creating a CSV file?
* Test round trip?



## Solution: Pytest test math functions
{id: pytest-solution-math}
![](examples/pytest/test_math.py)
![](examples/pytest/test_math_exceptions.py)



## Solution: Pytest test this app
{id: pytest-solution-app}
![](examples/pytest/test_app.py)


## Solution: test the csv module
{id: pytest-solution-csv}

![](examples/csv/csv_file_newline.csv)

![](examples/pytest/test_csv.py)

## PyTest using classes
{id: pytest-using-classes}

![](examples/pytest/test_with_class.py)
![](examples/pytest/test_with_class.out)


## PyTest failure reports
{id: pytest-failure-reports}

* Reporting success is boring
* Reporting failure can be interesting: assert + introspection



## PyTest compare numbers
{id: pytest-compare-numbers}
![](examples/pytest/test_number_equal.py)

```
    $ pytest test_number_equal.py

    def test_string_equal():
        assert double(2) == 4
>       assert double(21) == 42
E       assert 23 == 42
E        +  where 23 = double(21)
```



## PyTest compare numbers relatively
{id: pytest-compare-numbers-relatively}

![](examples/pytest/test_number_less_than.py)

```
$ pytest test_number_less_than.py
```

![](examples/pytest/test_number_less_than.out)


## PyTest compare strings
{id: pytest-compare-strings}

![](examples/pytest/test_string_equal.py)

```
$ pytest test_string_equal.py
```

![](examples/pytest/test_string_equal.out)


## PyTest compare long strings
{id: pytest-compare-long-strings}

![](examples/pytest/test_long_strings.py)

```
$ pytest test_long_strings.py
```

![](examples/pytest/test_long_strings.out)


## PyTest is one string in another strings
{id: pytest-in-strings}

Shows ~250 characters

![](examples/pytest/test_substring.py)
![](examples/pytest/test_substring.txt)


## PyTest test any expression
{id: pytest-any-expression}

![](examples/pytest/test_expression_equal.py)

```
$ pytest test_expression_equal.py

    def test_expression_equal():
        a = 3
>       assert a % 2 == 0
E       assert (3 % 2) == 0
```



## PyTest element in list
{id: pytest-element-in-list}

![](examples/pytest/test_in_list.py)

```
$ pytest test_in_list.py

    def test_in_list():
>       assert "dog" in get_list()
E       AssertionError: assert 'dog' in ['monkey', 'cat']
E        +  where ['monkey', 'cat'] = get_list()
```




## PyTest compare short lists
{id: pytest-compare-short-lists}
![](examples/pytest/test_short_lists.py)


```
$ pytest test_short_lists.py
```

```
    def test_short_lists():
>       assert get_lista() == get_listx()
E       AssertionError: assert ('a', 'b', 'c') == ('x', 'b', 'y')
E         At index 0 diff: 'a' != 'x'
E         Use -v to get the full diff
```


## PyTest compare short lists - verbose output
{id: pytest-compare-short-lists-verbose-output}

```
$ pytest -v test_short_lists.py
```

```
    def test_short_lists():
>       assert get_lista() == get_listx()
E       AssertionError: assert ('a', 'b', 'c') == ('x', 'b', 'y')
E         At index 0 diff: 'a' != 'x'
E         Full diff:
E         - ('a', 'b', 'c')
E         ?   ^         ^
E         + ('x', 'b', 'y')
E         ?   ^         ^
```

## PyTest compare lists
{id: pytest-compare-lists}

![](examples/pytest/test_lists.py)

```
$ pytest test_lists.py

    def test_long_lists():
>       assert get_list('a') == get_list('b')
E       AssertionError: assert ['0', '1', '2...'4', '5', ...]
            == ['0', '1', '2'...'4', '5', ...]
E         At index 100 diff: 'a' != 'b'
E         Use -v to get the full diff
```


## PyTest compare dictionaries - different values
{id: pytest-compare-dictionaries}

![](examples/pytest/test_dictionaries.py)

![](examples/pytest/test_dictionaries.out)

## PyTest compare dictionaries  - missing-keys
{id: pytest-compare-dictionaries-missing-keys}

![](examples/pytest/test_dictionaries_missing_keys.py)
![](examples/pytest/test_dictionaries_missing_keys.out)


## PyTest Fixtures
{id: pytest-fixture}

* In generally we call [test fixture](https://en.wikipedia.org/wiki/Test_fixture) the environment in which a test is expected to run.
* Pytest uses the same word for a more generic concept. All the techniques that make it easy to set up the environment and to tear it down after the tests.



## PyTest Fixture setup and teardown xUnit style
{id: pytest-fixture-setup-teardown}
{i: setup_function}
{i: teardown_function}
{i: setup_module}
{i: teardown_module}

![](examples/pytest/test_fixture.py)

See next slide for the output.


## PyTest Fixture setup and teardown output
{id: pytest-fixture-setup-teardown-output}

```
test_fixture.py .F.
```


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


Note, the teardown_function is executed even after failed tests.


## PyTest: Fixture Class setup and teardown
{id: pytest-class}
{i: setup_class}
{i: teardown_class}
{i: setup_method}
{i: teardown_method}

![](examples/pytest/test_class.py)


## PyTest: Fixture Class setup and teardown output
{id: pytest-class-output}

```
$ pytest -s test_class.py

setup_class called once for the class

setup_method called for every method
one
one after
teardown_method called for every method

setup_method called for every method
two
teardown_method called for every method

setup_method called for every method
three
three after
teardown_method called for every method

teardown_class called once for the class
```

## What is Dependency injection?
{id: pytest-dependency-injection}

```
def serve_bolognese(pasta, sauce):
    dish = mix(pasta, sauce)
    return dish
```


1. Find function.
1. Check parameters of the function.
1. Prepare the appropriate objects.
1. Call the function passing these objects.



## Pytest fixture - tmpdir
{id: pytest-tmpdir}
{i: tmpdir}

![](examples/pytest/test_tmpdir.py)

## Pytest CLI key-value store
{id: pytest-cli-key-value-store}

![](examples/pytest/key-value-store/store.py)
![](examples/pytest/key-value-store/test_store.py)

## Pytest testing key-value store - environment variable
{id: pytest-cli-testing-key-value-store}

![](examples/pytest/key-value-store-testable/store.py)
![](examples/pytest/key-value-store-testable/test_store.py)

## Pytest testing key-value store - environment variable (outside)
{id: pytest-cli-testing-key-value-store-outside}

![](examples/pytest/key-value-store-outside/store.py)
![](examples/pytest/key-value-store-outside/test_store.py)


## Pytest capture STDOUT and STDERR with capsys
{id: pytest-capsys}


Captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.

![](examples/pytest/greet.py)
![](examples/pytest/use_greet.py)

![](examples/pytest/test_greet.py)

```
pytest test_greet.py
```


## Pytest Fixture - home made fixtures - conftest
{id: pytest-home-made-fixture}
{i: conftest.py}

![](examples/pytest/fixtures.py)
![](examples/pytest/application.py)

```
$ pytest -s -q fixtures.py

getapp starts
__init__ of App
Working on add_user(Bar)
.shutdown of App cleaning up database
getapp ends

getapp starts
__init__ of App
Working on add_user(Foo)
.shutdown of App cleaning up database
getapp ends
```


## More fixtures
{id: pytest-more-fixtures}
![](examples/pytest/more_fixtures.py)
![](examples/pytest/more_fixtures.out)

* We can't add fixtures to test_functions as decorators (as I think was the case in NoseTest), we need to use dependency injection.



## Pytest: Mocking - why?
{id: pytest-mocking-why}

* Independent testing environment.
* Faster tests (mock remote calls, mock whole database)
* Fake some code/application/API that does not exist yet.
* Test error conditions in a system not under our control.



## Pytest: Mocking - what?
{id: pytest-mocking-what}

* External dependency (e.g. an API)
* STDIN/STDOUT/STDERR
* Random values
* Methods of a database



## Pytest: One dimensional spacefight
{id: pytest-number-guessing-game}
![](examples/pytest/game.py)


## Pytest: Mocking input and output
{id: pytest-test-game-exit}
![](examples/pytest/test_game_exit.py)


## Pytest: Mocking random
{id: pytest-test-game-play}
![](examples/pytest/test_game_play.py)




## Pytest: Flask echo
{id: pytest-flask-echo}
![](examples/pytest/flask_echo.py)


## Pytest: testing Flask echo
{id: pytest-testing-flask-echo}
![](examples/pytest/test_flask_echo.py)



## PyTest: Run tests in parallel with xdist
{id: pytest-run-test-in-parallel}
{i: xdist}

```
            $ pip install pytest-xdist
            $ pytest -n NUM
```




## PyTest: Order of tests
{id: pytest-order-of-test}


Pytest runs the test in the same order as they are found in the test module:


![](examples/pytest/test_order.py)

```
test_order.py::test_one PASSED
test_order.py::test_two PASSED
test_order.py::test_three PASSED
```


## PyTest: Randomize Order of tests
{id: pytest-randomize-order-of-test}

Install [pytest-random-order](https://pypi.python.org/pypi/pytest-random-order)

```
pip install pytest-random-order
```

And from now on all the test will run in a random order.


## PyTest: Force default order
{id: pytest-force-default-order}

If for some reason we would like to make sure the order remains the same,
we can add the following two lines of code.



```
import pytest
pytestmark = pytest.mark.random_order(disabled=True)
```
![](examples/pytest/test_default_order.py)


## PyTest: no random order
{id: pytest-no-random-order}

```
pytest -p no:random-order -v
```



## Anagram on the command line
{id: pytest-anagram-on-the-command-line}
![](examples/pytest/anagram.py)


## PyTest testing CLI
{id: pytest-test-cli}
![](examples/pytest/test_anagram.py)



## PyTest test discovery
{id: pytest-discovery}

Running py.test will find test files and in the files test functions.


* test_*.py files
* *_test.py files
* test_*  functions
* ...

![](examples/pytest/py.test.out)



## PyTest test discovery - ignore some tests
{id: pytest-test-discovery}

```
$ pytest


$ pytest --ignore venv3/
```

```
test_mymod_1.py .
test_mymod_2.py .F
```


* test_*.py files
* *_test.py files
* TestClasses
* test_*  functions
* ...

## Pytest dry-run - collect-only
{id: pytest-collect-only}

* Find all the test files, test classes, test functions that will be executed
* But don't run them

```
pytest --collect-only
```

## PyTest select tests by name
{id: pytest-select-by-name}
{i: --collect-only}
{i: -k}

* --collect-only - only list the tests, don't run them yet.
* -k select by name

![](examples/pytest/test_by_name.py)


```
pytest --collect-only test_by_name.py
    test_database_read
    test_database_write
    test_database_forget
    test_ui_access
    test_ui_forget
```


```
pytest --collect-only -k database test_by_name.py
    test_database_forget
    test_database_read
    test_database_write
```


```
pytest --collect-only -k ui test_by_name.py
    test_ui_access
    test_ui_forget
```


```
pytest --collect-only -k forget test_by_name.py
    test_database_forget
    test_ui_forget
```


```
pytest --collect-only -k "forget or read" test_by_name.py
    test_database_read
    test_database_forget
    test_ui_forget
```


## Pytest use markers
{id: pytest-use-markers}

![](examples/pytest/test_marker.py)
![](examples/pytest/test_marker.out)

* We need to declare them in the pytest.ini to avoid the warning

![](examples/pytest/pytest.ini)


## PyTest select tests by marker
{id: pytest-select-by-marker}
{i: --collect-only}
{i: -m}
{i: @pytest.mark}


* Use the @pytest.mark.name decorator to tag the tests.

![](examples/pytest/test_by_marker.py)

```
pytest --collect-only -m security test_by_marker.py
    test_ui_forget
    test_database_write
    test_database_forget
```

```
pytest --collect-only -m smoke test_by_marker.py
    test_database_read
    test_ui_access
    test_database_write
```

## No test selected
{id: no-test-selected}

{aside}
If you run pytest and it cannot find any tests, for example because you used some
selector and not test matched it, then Pytest will exit with exit code 5.

This is considered a failure by every tool, including Jenkins and other CI systems.

On the other hand you won't see any failed test reported. After all if no tests are run, then none of them fails.
This can be confusing.
{/aside}

```
$ pytest -k long test_by_marker.py

```

![](examples/pytest/no_test_selected.out)

```
$ echo $?
5
```



## PyTest: Test Coverage
{id: pytest-coverage}

```
pip install pytest-cov

pytest --cov=my --cov-report html --cov-branch

Open htmlcov/index.html
```

**Try werkzeug**

```
pytest --cov=werkzeug --cov-report html --cov-branch
xdg-open htmlcov/index.html
```


## Exercise: module
{id: pytest-exercise-module}

Pick one of the modules and write a test for it.

* [algo](https://github.com/JesperBry/algo)
* [editdistance](https://github.com/aflc/editdistance) Levenshtein distance implemented in C
* [python-Levenshtein](https://github.com/ztane/python-Levenshtein/) implemented in C
* [pylev](https://github.com/toastdriven/pylev)
* [pyxdameraulevenshtein](https://github.com/gfairchild/pyxDamerauLevenshtein)
* [weighted-levenshtein](https://github.com/infoscout/weighted-levenshtein)
* OpenPyXL


## Exercise: Open Source
{id: pytest-exercise-open-source}

* Visit the [stats](https://pydigger.com/stats) on PyDigger.com
* List the packages that [have GitHub no Travis-CI.](https://pydigger.com/search/has-github-no-travis-ci)
* Pick one that sounds simple. Visit its GitHub page and check if it has tests.
* If it does not, wirte one.
* Send Pull Request


## Pytest resources
{id: pytest-resources}

* [pytest.org](http://pytest.org/)
* [Python Testing with pytest by Brian Okken](https://pragprog.com/book/bopytest/python-testing-with-pytest) (The Pragmatic Bookshelf)
* [Python Testing by Brian Okken](http://pythontesting.net/)
* [Talk Python to me by Michael Kennedy](https://talkpython.fm/)
* [Python Bytes](https://pythonbytes.fm/) podcast by Brian Okken and Michael Kennedy


## Pytest and tempdir
{id: pytest-tempdir}

![](examples/pytest/mycfg.py)
![](examples/pytest/a.cfg)
![](examples/pytest/test_mycfg.py)

## PyTest compare short lists - output
{id: pytest-compare-short-lists-output}

![](examples/pytest/test_read_ini.py)

## PyTest with parameter
{id: pytest-with-parameter}
{i: @pytest.mark.parametrize}
{i: mark}
{i: parametrize}

![](examples/pytest/test_with_param.py)
![](examples/pytest/test_with_param.out)

## PyTest with parameters
{id: pytest-with-parameters}

![](examples/pytest/test_with_params.py)
![](examples/pytest/test_with_params.out)

## Pytest reporting in JUnit XML format
{id: python-reporting-in-juint-xml}

```
pytest --junitxml report.xml
```

* [pytest-json-report](https://pypi.org/project/pytest-json-report/)

```
pip install pytest-json-report

pytest --json-report --json-report-file=report.json
```

Recommended to also add

```
--json-report-omit=log
```

```
pytest -s --json-report --json-report-file=report.json --log-cli-level=INFO
```

![](examples/pytest/cases/test_one.py)

## Exercise: Write tests for script combining files
{id: exercise-write-tests-for-script-combining-file}

* This is a solution for one of the exercises in which we had to combine two files adding the numbers of the vegetables together.
* Many things could be improved, but before doing that, write a test (or two) to check this code. Without changing it.

![](examples/dictionary/combine_files.py)

Data Files:

![](examples/files/a.txt)
![](examples/files/b.txt)

## Solution: Write tests for script combining files
{id: solution-write-tests-for-script-combining-file}

* TBD
* Becaused we have fixed pathes in the script we have to create a directory structure that is similar to what is expected in a temporary location.
* Run the script and compare the results to some expected file.
* Then start refactoring the code.


## Add extra command line parameters to Pytest - conftest
{id: add-extra-command-line-parameters}
{i: conftest}

![](examples/pytest/py1/conftest.py)
![](examples/pytest/py1/test_one.py)

![](examples/pytest/py2/conftest.py)
![](examples/pytest/py2/test_one.py)

![](examples/pytest/py3/conftest.py)
![](examples/pytest/py3/test_one.py)

![](examples/pytest/py4/conftest.py)
![](examples/pytest/py4/test_one.py)

## Pytest and forking
{id: pytest-and-forking}

* This tests passes and generates two reports.
* I could not find a way yet to avoid the reporting in the child-process. Maybe we need to run this with a special runner that will fork and run this test on  our behalf.

![](examples/pytest/test_forker.py)



## Pytest forking code
{id: pytest-forking-code}

![](examples/pytest/fork/app.py)
![](examples/pytest/fork/test_app.py)

