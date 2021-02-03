# PyTest Fixtures
{id: pytest-fixture}


## PyTest What are Fixtures
{id: pytest-what-are-fixture}

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



