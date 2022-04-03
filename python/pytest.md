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

* Test methods of the [math](https://docs.python.org/library/math.html) module.
* ceil
* factorial
* gcd




## Exercise: test this app
{id: pytest-exercise-app}


Write tests for the `swap` and `average` functions of the `app` module. Can you find a bug?


![](examples/pytest/app.py)


## Exercise: test the csv module
{id: pytest-exercise-csv}

* [csv](https://docs.python.org/library/csv.html)
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


## parametrize PyTest with pytest.mark.parametrize
{id: pytest-with-parameter}
{i: @pytest.mark.parametrize}
{i: mark}
{i: parametrize}

![](examples/pytest/test_with_param.py)
![](examples/pytest/test_with_param.out)

## parametrize PyTest with multiple parameters
{id: pytest-with-parameters}

![](examples/pytest/test_with_params.py)
![](examples/pytest/test_with_params.out)

## Pytest and forking
{id: pytest-and-forking}

* This tests passes and generates two reports.
* I could not find a way yet to avoid the reporting in the child-process. Maybe we need to run this with a special runner that will fork and run this test on  our behalf.


![](examples/pytest/fork/app.py)
![](examples/pytest/fork/test_app.py)

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


## Pytest: Flask echo
{id: pytest-flask-echo}

![](examples/pytest/flask_echo.py)


## Pytest: testing Flask echo
{id: pytest-testing-flask-echo}

![](examples/pytest/test_flask_echo.py)

## Pytest resources
{id: pytest-resources}

* [pytest.org](http://pytest.org/)
* [Python Testing with pytest by Brian Okken](https://pragprog.com/book/bopytest/python-testing-with-pytest) (The Pragmatic Bookshelf)
* [Python Testing by Brian Okken](http://pythontesting.net/)
* [Talk Python to me by Michael Kennedy](https://talkpython.fm/)
* [Python Bytes](https://pythonbytes.fm/) podcast by Brian Okken and Michael Kennedy


## Anagram on the command line
{id: pytest-anagram-on-the-command-line}
![](examples/pytest/anagram.py)


## PyTest testing CLI
{id: pytest-test-cli}
![](examples/pytest/test_anagram.py)





