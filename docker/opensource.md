# Open Source
{id: open-source}

## TOML Kit
* [tomlkit](https://github.com/sdispater/tomlkit)

Steps to run tests on a docker container:
```
git clone --recurse-submodules https://github.com/sdispater/tomlkit.git
cd tomlkit
docker run -it --name toml -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
pip install pytest
poetry install
poetry run pytest -q tests
```

## Dialogy
* [Dialogy](https://github.com/skit-ai/dialogy)

Steps to run tests on a docker container:
```
git clone https://github.com/skit-ai/dialogy.git
cd dialogy
docker run -it --name dialogy -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
make install
```

## Teiphy
* [Teiphy](https://github.com/jjmccollum/teiphy)

Steps to run tests on a docker container:
```
git clone https://github.com/jjmccollum/teiphy.git
cd teiphy
docker run -it --name teiphy -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
pip install pytest
poetry install
poetry run pytest
```

## Python Automation Framework
* [python-automation-framework](https://github.com/mreiche/python-automation-framework)

Steps to run tests on a docker container:
```
git clone https://github.com/mreiche/python-automation-framework.git
cd python-automation-framework
docker run -it --name python-automation-framework -w /opt -v$(pwd):/opt python:3.11 bash
pip install pytest
PYTHONPATH="." pytest --numprocesses=4 --cov=paf test
```

## Python Bitcoinlib
* [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)

Steps to run tests on a docker container:
```
git clone https://github.com/petertodd/python-bitcoinlib.git
cd python-bitcoinlib
docker run -it --name python-bitcoinlib -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover
```

## Overloaded Iterables
* [overloaded_iterables](https://github.com/Arkiralor/overloaded_iterables)

Steps to run tests on a docker container:
```
git clone https://github.com/Arkiralor/overloaded_iterables.git
cd overloaded_iterables
docker run -it --name overloaded_iterables -w /opt -v$(pwd):/opt python:3.11 bash
chmod +x scripts/*
sh scripts/run_tests.sh
```

## xapi-python
* [xapi-python](https://github.com/pawelkn/xapi-python)

Steps to run tests on a docker container:
```
git clone https://github.com/pawelkn/xapi-python.git
cd xapi-python
docker run -it --name xapi-python -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover tests
```

## nats-python
* [nats-python](https://github.com/Gr1N/nats-python)

Steps to run tests on a docker container:
```
git clone https://github.com/Gr1N/nats-python.git
cd nats-python
docker run -it --name nats-python -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
make install 
make test
```

## Python Flask
{id: docker-python-flask}


* [Flask](https://github.com/pallets/flask)
* Has a file called `CONTRIBUTING.rst`

```
$ git clone https://github.com/pallets/flask.git
$ cd flask
$ docker run -it --name flask-dev -w /opt -v$(pwd):/opt python:3.11 bash

# python -m pip install -U pip setuptools wheel
# pip install -r requirements/dev.txt && pip install -e .
# pytest
```

```
$ docker start -i flask-dev
```

## Python requests
{id: docker-python-requests}

* [Development environment for the Python requests package](https://dev.to/szabgab/development-environment-for-the-python-requests-package-eae)

## R data.table
{id: docker-r-data-table}

* [data.table]()
* [Local development environment for the data.table R project](https://dev.to/szabgab/local-development-environment-for-the-datatable-r-project-5fhb)

```
$ git clone git@github.com:Rdatatable/data.table.git
$ cd data.table
$ docker run -it --name data-table --workdir /opt -v$(pwd):/opt r-base:4.2.3 bash

# apt-get update
# apt-get install -y pandoc curl libcurl4-gnutls-dev texlive-latex-base texlive-fonts-extra texlive-latex-recommended texlive-fonts-recommended
# Rscript -e 'install.packages(c("knitr", "rmarkdown", "pandoc", "curl", "bit64", "bit", "xts", "nanotime", "zoo", "R.utils", "markdown"))'
# R CMD build .
```

Check the version number in the name of the generated tar.gz file:

```
# ls -l
# R CMD check data.table_1.14.9.tar.gz
```

This would work without checking

```
# R CMD check $(ls -1 data.table_*)
```


```
$ docker container start -i data-table
```

## R yaml
{id: docker-r-yaml}

* [Setup local development environment for R-yaml](https://dev.to/szabgab/setup-local-development-environment-for-r-yaml-5ejc)


## PHP Twig
{id: docker-php-twig}

* [Twig](https://github.com/twigphp/Twig)
* [Setup local development environment and run tests of PHP Twig](https://dev.to/szabgab/setup-local-development-environment-and-run-tests-of-php-twig-34d3)

```
$ git clone git@github.com:twigphp/Twig.git
$ docker run -it --rm --workdir /opt -v$(pwd):/opt ubuntu:22.10 bash

# apt-get update
# DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
# apt-get install -y php-cli composer php-curl phpunit

# composer install
# phpunit
```



