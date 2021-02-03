# Pytest command line options
{id: pytest-options}

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


