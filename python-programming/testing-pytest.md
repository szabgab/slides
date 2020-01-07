# Testing with PyTest
{id: testing-with-pytest}

## Pytest features
{id: pytest-features}

* Organize and run test per directory (test discovery)
* Run tests by name matching
* Run tests by mark (smoke, integration, db)
* Run tests in parallel with the xdist plugin.
* Create your own fixtures and distribute them.
* Create your own plugins and distribute them.



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


## Testing with Pytest
{id: pytested-module}


A module called `mymath` with two functions: `add` and `div`.


![](examples/pytest/mymath.py)


## Testing functions
{id: pytest-module}
![](examples/pytest/test_mymath.py)


## Testing class and methods
{id: pytest-module-class}
![](examples/pytest/test_mymath_class.py)


## Pytest - execute
{id: pytest-run-tests}

```
pytest test_mymath.py
<include file="examples/pytest/test_mymath.out" />
```


## Pytest - execute
{id: pytest-execute}

```
pytest
python -m pytest
```


## Pytest simple module to be tested
{id: pytest-simple-module-to-be-tested}


An anagram is a pair of words containing the exact same letters in different order. For example:



* listen silent
* elvis lives


![](examples/pytest/mymod_1.py)


## Pytest simple tests - success
{id: pytest-simple-success}
{i: assert}
{i: pytest}
![](examples/pytest/test_mymod_1.py)


## Pytest simple tests - success output
{id: pytest-simple-success-output}

```
$ pytest test_mymod_1.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 1 items

test_mymod_1.py .

=================== 1 passed in 0.03 seconds ===================
```


## Pytest simple tests - failure
{id: pytest-simple-failure}

* Failure reported by user: **is_anagram("anagram", "nag a ram")** is expected to return true.
* We write a test case to reproduce the problem. It should fail now.

![](examples/pytest/test_mymod_2.py)


## Pytest simple tests - failure output
{id: pytest-simple-failure-output}

```
$ pytest test_mymod_2.py

===================== test session starts ======================
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /examples/python/pt, inifile:
collected 2 items

test_mymod_2.py .F

=========================== FAILURES ===========================
____________________ test_multiword_anagram ____________________

    def test_multiword_anagram():
       assert is_anagram("ana gram", "naga ram")
>      assert is_anagram("anagram", "nag a ram")
E      AssertionError: assert False
E       +  where False = is_anagram('anagram', 'nag a ram')

test_mymod_2.py:10: AssertionError
============== 1 failed, 1 passed in 0.09 seconds ==============
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



## PyTest bank deposit
{id: pytest-bank-deposit}
![](examples/pytest/b1/banks.py)


## PyTest expected exceptions (bank deposit)
{id: pytest-expected-exceptions-bank-deposit}
![](examples/pytest/b1/test_bank.py)

```
pytest test_bank.py

test_bank.py .
```


## PyTest expected exceptions (bank deposit) - no exception happens
{id: pytest-expected-exceptions-bank-deposit-no-exception}

Pytest properly reports that there was no exception where an exception was expected.


![](examples/pytest/b2/banks.py)
![](examples/pytest/b2/error.txt)


## PyTest expected exceptions (bank deposit) - different exception is raised
{id: pytest-expected-exceptions-bank-deposit-different-exception}
![](examples/pytest/b3/banks.py)
![](examples/pytest/b3/error.txt)


## PyTest expected exceptions
{id: pytest-expected-exceptions}
![](examples/pytest/test_exceptions.py)


## PyTest expected exceptions output
{id: pytest-expected-exceptions-output}

```
$ pytest test_exceptions.py

test_exceptions.py .
```


## PyTest expected exceptions (text changed)
{id: pytest-expected-exceptions-test-changed}
![](examples/pytest/test_exceptions_text_changed.py)


## PyTest expected exceptions (text changed) output
{id: pytest-expected-exceptions-test-changed-output}

```
$ pytest test_exceptions_text_changed.py


    def test_zero_division():
        with pytest.raises(ValueError) as e:
            divide(1, 0)
>       assert str(e.value) == 'Cannot divide by Zero'
E       AssertionError: assert 'Cannot divide by Null' == 'Cannot divide by Zero'
E         - Cannot divide by Null
E         ?                  ^^^^
E         + Cannot divide by Zero
E         ?                  ^^^^
```


## PyTest expected exceptions (other exception)
{id: pytest-expected-exceptions-failure}
![](examples/pytest/test_exceptions_failing.py)


## PyTest expected exceptions (other exception) output
{id: pytest-expected-exceptions-failure-output}

```
    $ pytest test_exceptions_failing.py

    def test_zero_division():
        with pytest.raises(ValueError) as e:
>           divide(1, 0)

test_exceptions_failing.py:10:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 1, b = 0

    def divide(a, b):
    #    if b == 0:
    #        raise ValueError('Cannot divide by Zero')
>       return a / b
E       ZeroDivisionError: division by zero
```


## PyTest expected exceptions (no exception)
{id: pytest-expected-exceptions-no-exception}
![](examples/pytest/test_exceptions_missing.py)


## PyTest expected exceptions (no exception) output
{id: pytest-expected-exceptions-no-exception-output}

```
    def test_zero_division():
        with pytest.raises(ValueError) as e:
>           divide(1, 0)
E           Failed: DID NOT RAISE <class 'ValueError'>
```






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
pytest test_mymod_2.py::test_anagram

pytest test_mymod_2.py::test_multiword_anagram
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


## Pytest: show skipped tests woth -rs
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

    def test_string_equal():
>       assert get_number() < 0
E       assert 23 < 0
E        +  where 23 = get_number()
```


## PyTest compare strings
{id: pytest-compare-strings}
![](examples/pytest/test_string_equal.py)

```
$ pytest test_string_equal.py

    def test_string_equal():
>       assert get_string() == "abd"
E       AssertionError: assert 'abc' == 'abd'
E         - abc
E         + abd
```


## PyTest compare long strings
{id: pytest-compare-long-strings}
![](examples/pytest/test_long_strings.py)

```
$ pytest test_long_strings.py

    def test_long_strings():
>       assert get_string('a') == get_string('b')
E       AssertionError: assert '0123456789ab...t\n\r\x0b\x0c' == '0123456789abc...t\n\r\x0b\x0c'
E         Skipping 90 identical leading characters in diff, use -v to show
E         Skipping 91 identical trailing characters in diff, use -v to show
E           {|}~
E
E         - a012345678
E         ? ^
E         + b012345678
E         ? ^
```


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


## PyTest compare dictionaries
{id: pytest-compare-dictionaries}
![](examples/pytest/test_dictionaries.py)


## PyTest compare dictionaries output
{id: pytest-compare-dictionaries-output}

```
$ pytest test_dictionaries.py

______________ test_big_dictionary_different_value _______________

    def test_big_dictionary_different_value():
>       assert get_dictionary('a', 'def') == get_dictionary('a', 'abc')
E       AssertionError: assert {'\t': 9, '\n...x0c': 12, ...}
          == {'\t': 9, '\n'...x0c': 12, ...}
E         Omitting 99 identical items, use -v to show
E         Differing items:
E         {'a': 'def'} != {'a': 'abc'}
E         Use -v to get the full diff

_______________ test_big_dictionary_differnt_keys ________________

    def test_big_dictionary_differnt_keys():
>       assert get_dictionary('abc', 1) == get_dictionary('def', 2)
E       AssertionError: assert {'\t': 9, '\n...x0c': 12, ...}
           == {'\t': 9, '\n'...x0c': 12, ...}
E         Omitting 100 identical items, use -v to show
E         Left contains more items:
E         {'abc': 1}
E         Right contains more items:
E         {'def': 2}
E         Use -v to get the full diff
```


## PyTest Fixtures
{id: pytest-fixture}

* In generally we call [test fixture](https://en.wikipedia.org/wiki/Test_fixture) the environment in which a test is expected to run.
* Pytest uses the same word for a more generic concept. All the techniques that make it easy to set up the environment and to tear it down after the tests.



## PyTest Fixture setup and teardown
{id: pytest-fixture-setup-teardown}
{i: setup_function}
{i: terdown_function}
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




## PyTest: Class setup and teardown
{id: pytest-class}
![](examples/pytest/test_class.py)


## PyTest: Class setup and teardown output
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



## Pytest Dependency injection
{id: pytest-dependency-injection}

```
def function(thingy):
   pass
```


1. Find function.
1. Check parameters of the function.
1. Create the appropriate instances.
1. Call the function with the intsances.



## Pytest fixture - tmpdir
{id: pytest-tmpdir}
{i: tmpdir}
![](examples/pytest/test_tmpdir.py)


## Pytest capture STDOUT and STDERR with capsys
{id: pytest-capsys}


Captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.


![](examples/pytest/capture.py)



## Pytest Fixture - home made fixtures
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




## PyTest select tests by name
{id: pytest-select-by-name}
{i: --collect-only}
{i: -k}

* --collect-only - only list the tests, don't run them yet.
* -k select by name

![](examples/pytest/test_by_name.py)

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


## PyTest select tests by marker
{id: pytest-select-by-marker}
{i: --collect-only}
{i: -m}
{i: @pytest.mark}


 Use the @pytest.mark.name decorator to tag the tests.


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






