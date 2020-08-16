# Python
{id: travis-ci-for-python}

## Travis-CI and Python
{id: travis-ci-and-python}
{i: python}

* [Travis-CI and Python](https://docs.travis-ci.com/user/languages/python/)

* `language: python`
* `pip install -r requirements.txt` is executed automatically
* empty `requirements.txt` file will do it.

![](examples/python-plain/.travis.yml)

## Travis-CI and Python with Pytest
{id: travis-ci-and-python-with-pytest}
{i: python}

* Simply adding `script: pytest` will not work.
* pytest will fail with exit code 5 if it cannot find any test to run.

![](examples/python-pytest/.travis.yml)
![](examples/python-pytest/test_python.py)

## Python version matrix
{id: python-version-matrix}

![](examples/python-version-matrix/.travis.yml)
![](examples/python-version-matrix/test_python.py)

## The environment variables set by Travis - Python
{id: environment-variables-set-by-travis-python}
{i: environ}
{i: os.environ}

* [Environment variables](https://docs.travis-ci.com/user/environment-variables/)

![](examples/python-environment-variables/.travis.yml)

![](examples/python-environment-variables/test_python.py)

## Set environment variables for Python
{id: set-environment-variables-for-python}

![](examples/python-set-environment-variables/.travis.yml)
![](examples/python-set-environment-variables/test_python.py)

## Python version and environment matrix
{id: python-version-and-environment-matrix}
{i: matrix}

![](examples/python-env-version-matrix/.travis.yml)

![](examples/python-env-version-matrix/test_python.py)

![](examples/python-env-version-matrix/pytest.ini)

