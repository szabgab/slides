# Pytest command line options
{id: pytest-options}

## PyTest: Run tests in parallel with xdist
{id: pytest-run-test-in-parallel}
{i: xdist}

```
$ pip install pytest-xdist
$ pytest -n NUM
```

![](examples/pytest/xdist/test_animals.py)
![](examples/pytest/xdist/test_colors.py)

```
pytest          8.04 sec
pytest -n 2     4.64 sec
pytest -n 4     3.07 sec
```


## PyTest: Order of tests
{id: pytest-order-of-test}


Pytest runs the test in the same order as they are found in the test module:


![](examples/pytest/order/test_order.py)

```
pytest -v

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

And from now we can use the `--random-order` flag to run the tests in a random order.

```
pytest -v --random-order

test_order.py::test_two PASSED
test_order.py::test_three PASSED
test_order.py::test_one PASSED
```


## PyTest: Force default order
{id: pytest-force-default-order}

If for some reason we would like to make sure the order remains the same,
in a given module, we can add the following two lines of code.


```
import pytest
pytestmark = pytest.mark.random_order(disabled=True)
```
![](examples/pytest/order/test_default_order.py)


## PyTest test discovery
{id: pytest-discovery}

Running pytest will find test files and in the files test functions.


* test_*.py files
* *_test.py files
* test_*  functions
* TestSomething class
*   test_* methods

```
examples/pytest/discovery
.
├── db
│   └── test_db.py
├── other_file.py
├── test_one.py
└── two_test.py

```

![](examples/pytest/discovery.out)



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

## Pytest dry-run - collect-only
{id: pytest-collect-only}

* Find all the test files, test classes, test functions that will be executed.
* But don't run them...
* ...  but they are still loaded into memory so any code in the "body" of the files is executed.

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


## Pytest use markers to select tests
{id: pytest-use-markers}

* -m select by mark

![](examples/pytest/markers/test_marker.py)
![](examples/pytest/markers/test_marker.out)

* We need to declare them in the pytest.ini to avoid the warning

![](examples/pytest/markers/pytest.ini)


## PyTest select tests by marker
{id: pytest-select-by-marker}
{i: --collect-only}
{i: -m}
{i: @pytest.mark}


* Use the @pytest.mark.name decorator to tag the tests.

![](examples/pytest/markers/test_by_marker.py)

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

## Pytest reporting in JUnit XML or JSON format
{id: pytest-reporting}

![](examples/pytest/reporting/test_colors.py)


## Pytest reporting in JUnit XML format
{id: pytest-reporting-in-juint-xml}

* e.g. for Jenkins integration
* See [usage](https://docs.pytest.org/en/stable/usage.html)

```
pytest --junitxml report.xml
```

![](examples/pytest/reporting/report.xml)

To make the XML more himan-readable:

```
cat report.xml | python -c 'import sys;import xml.dom.minidom;s=sys.stdin.read();print(xml.dom.minidom.parseString(s).toprettyxml())'
```


## Pytest reporting in JSON format
{id: pytest-reporting-in-json}


* [pytest-json-report](https://pypi.org/project/pytest-json-report/)

```
pip install pytest-json-report

pytest --json-report --json-report-file=report.json --json-report-indent=4
```

Recommended to also add

```
--json-report-omit=log
```

```
pytest -s --json-report --json-report-file=report.json --log-cli-level=INFO
```

## Pytest JSON report
{id: pytest-json-repor}

![](examples/pytest/reporting/report.json)

## Add extra command line parameters to Pytest - conftest - getoption
{id: add-extra-command-line-parameters}
{i: conftest}

* In this case the option expects a value
* And we need to use getoption to get the value
* See [Parser](https://docs.pytest.org/en/stable/reference.html#parser)
* See [argparse](https://docs.python.org/library/argparse.html)

![](examples/pytest/py1/conftest.py)
![](examples/pytest/py1/test_one.py)

```
pytest -s
None
False
```

```
pytest -s --demo Hello --noisy
Hello
True
```

## Add extra command line parameters to Pytest - as a fixture
{id: add-extra-command-line-parameters-as-a-fixture}
{i: conftest}

* We can also create a fixture that will read the parameter

![](examples/pytest/py2/conftest.py)
![](examples/pytest/py2/test_one.py)

```
pytest -s
test_one.py None
```

```
pytest -s --demo Hello
test_one.py Hello
```

## Add extra command line parameters to Pytest - used in the autouse fixtures
{id: add-extra-command-line-parameters-autouse-fixture}
{i: conftest}


![](examples/pytest/py4/conftest.py)
![](examples/pytest/py4/test_one.py)

```
pytest -s --demo Hello

Module Hello
Func Hello
Func Hello
```

## PyTest: Test Coverage
{id: pytest-coverage}


![](examples/pytest/coverage/mymod.py)
![](examples/pytest/coverage/test_mymod.py)

```
pip install pytest-cov

pytest --cov=mymod --cov-report html --cov-branch

Open htmlcov/index.html
```
