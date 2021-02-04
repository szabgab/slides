# PyTest Fixtures
{id: pytest-fixtures}


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

![](examples/pytest/test_tmpdir.py)

## Pytest and tempdir
{id: pytest-tempdir}

![](examples/pytest/mycfg.py)
![](examples/pytest/a.cfg)
![](examples/pytest/test_mycfg.py)


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


## Application that prints to STDOUT and STDERR
{id: pytest-application-stdout-stderr}


![](examples/pytest/greet.py)
![](examples/pytest/use_greet.py)
![](examples/pytest/use_greet.out)

## Pytest capture STDOUT and STDERR with capsys
{id: pytest-capsys}

Captures everything that is printed to STDOUT and STDERR so we can compare that to the expected output and error.

![](examples/pytest/test_greet.py)

```
pytest test_greet.py
```

## Pytest Fixture - autouse fixtures
{id: pytest-autouse-fixture}
{i: yield}

* Similar to `setup_function`, `teardown_function`, `setup_module`, `teardown_module`

![](examples/pytest/autouse_fixtures.py)
![](examples/pytest/autouse_fixtures.out)

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

![](examples/pytest/manual_fixtures.py)
![](examples/pytest/manual_fixtures.out)

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

