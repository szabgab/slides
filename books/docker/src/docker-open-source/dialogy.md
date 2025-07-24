# Dialogy

* [Dialogy](https://github.com/skit-ai/dialogy)

Steps to run tests on a docker container:

```
git clone https://github.com/skit-ai/dialogy.git
cd dialogy
docker run -it --name dialogy -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
make install
make test
```

from Readme.md -> Contributors

```
git clone git@github.com:skit-ai/dialogy.git
cd dialogy
docker run -it --name dialogy_test -w /opt -v <working directory>\dialogy:/opt python:3.11 bash
# Activate your virtualenv, you can also let poetry take care of it.
$ pip install poetry (opened a [PR](https://github.com/skit-ai/dialogy/pull/194)) for adding this command
$ poetry install
$ make test
```



