# PyTest Fixtures
{id: pytest-fixtures}

## PyTest: What are Fixtures?
{id: pytest-what-are-fixture}

* In generally we call [test fixture](https://en.wikipedia.org/wiki/Test_fixture) the environment in which a test is expected to run.
* Pytest uses the same word for a more generic concept. All the techniques that make it easy to set up the environment and to tear it down after the tests.

General examples:

* Setting up a database server - then removing it to clean the machine.
* Maybe filling the database server with some data - emptying the database.

Specific examples:

* If I'd like to test the login mechanism, I need that before the test starts running we'll have a verified account in the system.
* If I test the 3rd element in a pipeline I need the results of the 2nd pipeline to get started and after the test runs I need to remove all those files.

## PyTest: test with functions
{id: pytest-test-with-functions}

If we don't have any of the fixture services we need to write a lot of code:

* We need to call the `setup_db()` in every test.
* We need to call the `teardown_db()` in every test - and it still does not work when the test fails.
* What if there is some work that needs to be done only once and not for every test?

![](examples/pytest/test_functions.py)

![](examples/pytest/test_functions.out)


## PyTest Fixture setup and teardown xUnit style
{id: pytest-fixture-setup-teardown}
{i: setup_function}
{i: teardown_function}
{i: setup_module}
{i: teardown_module}

{aside}
There are two mechanism in PyTest to setup and teardown fixtures. One of them is the xUnit-style system that is also available in other languages such as Java and C#.

In this example there are 3 tests, 3 functions that are called `test_SOMETHING`. There are also two pairs of functions to setup and teardown the fixtures on a per-function and per-module level.

Before starting to run the tests of this file PyTest will run the `setup_module` function, and after it is done running the tests PyTest will run the `teardonw_module` function. This will happen even if one or more of the tests failed.  These functions will be called once regradless of the number of tests we have in the module.

Before every test function PyTest will run the `setup_function` and after the test finisihed it will run the `teardown_function`. Regardless of the success or failure of the test.

So in our case where we have all 4 of the fixture functions implemented and we have 3 tests function the order can be seen on the next page.

In this example we also see one of the major issues of this style. The variable `db` that is set in the setup_module function must be marked as `global` in order to make it accessible in the test functions and in the `teardown_module` function.
{/aside}

![](examples/pytest/test_fixture.py)

See next slide for the output.


## PyTest Fixture setup and teardown output
{id: pytest-fixture-setup-teardown-output}

```
test_fixture.py .F.
```

```
$ pytest -sq test_fixture.py

```

![](examples/pytest/test_fixture.out)

Note, the teardown_function is executed even after failed tests.


## PyTest: Fixture Class setup and teardown
{id: pytest-class}
{i: setup_class}
{i: teardown_class}
{i: setup_method}
{i: teardown_method}

{aside}
In case you are using test classes then you can use another 2 pairs of functions, well actually methods, to setup and teardown the environment.
In this case it is much easier to pass values from the setup to the test functions and to the teardown function, but we need to write the whole thing in
OOP style.

Also note, the test functions are independent. They all see the atributes set in the `setup_class`, but the test functions cannot pass values to each other.
{/aside}

![](examples/pytest/test_class.py)


## PyTest: Fixture Class setup and teardown output
{id: pytest-class-output}

```
$ pytest -sq test_class.py
```

![](examples/pytest/test_class.out)

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

* Probably the simples fixture that PyTest can provide is the `tmpdir`.
* Pytest will prepare a temporary directory and call the test function passing the path to the `tmpdir`.
* PyTest will also clean up the temporary folder, though it will keep the 3 most recent ones. (this is configurable)

![](examples/pytest/test_tmpdir.py)

## Pytest and tempdir
{id: pytest-tempdir}
{i: tmpdir}

* This is a simple application that reads and writes config files (ini file).
* We can test the `parse_file` by preparing some input files and check if we get the expected data structure.
* In order to test the `save_file` we need to be able to save a file somewhere.
* Saving it in the current folder will create garbage files. (and the folder might be read-only in some environments).
* For each test we'll have to come up with a separate filename so they won't collide.
* Using a `tmpdir` solves this problem.

![](examples/pytest/mycfg.py)
![](examples/pytest/a.cfg)
![](examples/pytest/test_mycfg.py)


## Pytest CLI key-value store
{id: pytest-cli-key-value-store}

* This is a similar application - a file-base key-value store - where the data files is computed from the name of the program: `store.json`.
* Runing two tests in parallel will make the tests collide by using the same data file.

![](examples/pytest/key-value-store/store.py)
![](examples/pytest/key-value-store/test_store.py)

## Pytest testing key-value store - environment variable
{id: pytest-cli-testing-key-value-store}

* We need to be able to set the name of the data file externally. e.g. Using an environment variable.

![](examples/pytest/key-value-store-testable/store.py)
![](examples/pytest/key-value-store-testable/test_store.py)

## Pytest testing key-value store - environment variable (outside)
{id: pytest-cli-testing-key-value-store-outside}

![](examples/pytest/key-value-store-outside/store.py)
![](examples/pytest/key-value-store-outside/test_store.py)


## Application that prints to STDOUT and STDERR
{id: pytest-application-stdout-stderr}


![](examples/pytest/greet.py)
![](examples/pytest/use_greet.py)
![](examples/pytest/use_greet.out)

## Pytest capture STDOUT and STDERR with capsys
{id: pytest-capsys}
{i: capsys}

Captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.

![](examples/pytest/test_greet.py)

```
pytest test_greet.py
```

## PyTest - write your own fixture
{id: pytest-write-your-own-fixture}

* `tmpdir` and `capsys` are nice to have, but we will need more complex setup and teardown.

* We can write any function to become fixture, we only need to decorate it with `@pytest.fixture`

* We can implement fixture functions to act like the xUnit fixture we saw ealrier or using dependency injection as `tmpdir` and `capsys` work.


## Pytest Fixture - autouse fixtures
{id: pytest-autouse-fixture}
{i: yield}

* Similar to `setup_function`, `teardown_function`, `setup_module`, `teardown_module`

![](examples/pytest/test_autouse_fixtures.py)
![](examples/pytest/test_autouse_fixtures.out)

## Share fixtures among test files: conftest.py
{id: pytest-conftest}
{i: conftest.py}

![](examples/pytest/autouse/conftest.py)
![](examples/pytest/autouse/test_blue.py)
![](examples/pytest/autouse/test_green.py)

```
pytest -qs
```
![](examples/pytest/autouse/pytest.out)


## Manual fixtures (dependency injection)
{id: pytest-manual-fixtures}

![](examples/pytest/test_manual_fixtures.py)
![](examples/pytest/test_manual_fixtures.out)

* We can't add fixtures to test_functions as decorators (as I was the case in NoseTest), we need to use dependency injection.

## Pytest Fixture providing value
{id: pytest-fixture-providing-value}

![](examples/pytest/fixture-with-value/test_app.py)
![](examples/pytest/fixture-with-value/application.py)

```
$ pytest -sq
```

![](examples/pytest/fixture-with-value/test_app.out)

## Pytest Fixture providing value with teardown
{id: pytest-fixture-providing-value-with-teardown}

![](examples/pytest/fixture-with-teardown/test_app.py)
![](examples/pytest/fixture-with-teardown/application.py)

```
$ pytest -sq
```

![](examples/pytest/fixture-with-teardown/test_app.out)


## Pytest create fixture with file(s) - app and test
{id: pytest-create-fixture-with-files-app-and-test}


![](examples/pytest/configfile/myapp.py)
![](examples/pytest/configfile/config.json)
![](examples/pytest/configfile/use_myapp.py)
![](examples/pytest/configfile/out.txt)

* Test application

![](examples/pytest/configfile/test_app.py)

## Pytest create fixture with file(s) - helper function
{id: pytest-create-fixture-with-files-helper-function}

![](examples/pytest/configfile/test_app_function.py)

## Pytest create fixture with file(s) - fixture
{id: pytest-create-fixture-with-files-fixture}
![](examples/pytest/configfile/test_app_fixture.py)


## Pytest with Docker - application
{id: pytest-with-docker-application}

![](examples/pytest/docker/app.py)
![](examples/pytest/docker/test_app.py)


## Pytest with Docker  - test
{id: pytest-with-docker-test}

![](examples/pytest/docker/Dockerfile)
![](examples/pytest/docker/.dockerignore)
![](examples/pytest/docker/test_with_docker.py)

## Pytest with Docker  - improved
{id: pytest-with-docker-improved}

![](examples/pytest/docker/test_with_docker_improved.py)

## Pytest fixture inject data
{id: pytest-fixture-inject-data}

![](examples/pytest/test_fixture_inject.py)

## Pytest fixture for MongoDB
{id: pytest-fixture-mongodb}

![](examples/pytest/fixture-mongodb/conftest.py)

## Pytest parameters
{id: pytest-parameters}

![](examples/pytest/test_mymath_parameters.py)

## Pytest parametrized fixture
{id: pytest-parametrized-fixture}

{aside}
Sometimes we would like to pass some parameters to the fixture. We can do this with one or more parameters.
{/aside}

![](examples/pytest/test_parametrized_fixture.py)
![](examples/pytest/test_parametrized_fixture.out)

## Pytest parametrized fixture with dependency injection
{id: pytest-parametrized-fixture-with-dependency-injection}


![](examples/pytest/test_parametrized_injection_fixture.py)
![](examples/pytest/test_parametrized_injection_fixture.out)

## Pytest parametrized fixture to use Docker
{id: pytest-parametrized-fixture-to-use-docker}

{aside}
I created a GitHub Action for the [OSDC site generator](https://github.com/OSDC-Code-Maven/osdc-site-generator) which is running inside a Docker container.
At one point I wanted the whole image creation and running in the image be part of the test.
{/aside}

![](examples/pytest/test_parametrized_fixture_with_docker.py)


