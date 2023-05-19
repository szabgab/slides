# Open Source
{id: open-source}

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
## Plagiarism-checker-Python
{id: docker-plagiarism-checker-python}

```
$ git clone https://github.com/Kalebu/Plagiarism-checker-Python
$ cd Plagiarism-checker-Python
$ docker run -it --name Renormalizer-devPlagiarism-checker-Python -w /opt -v %cd%:/opt python:latest bash
$ pip3 install -r requirements.txt
```

running the project

```
$ python3 app.py
('john.txt', 'juma.txt', 0.5465972177348937)
('fatma.txt', 'john.txt', 0.14806887549598566)
('fatma.txt', 'juma.txt', 0.18643448370323362)
```

## Cosmo-Tech
{id: docker-python-cosmo-tech}


* [Cosmo-Tech](https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library)

```
$ git clone https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library.git
$ cd CosmoTech-Acceleration-Library
```

For Windows:
CMD:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name cosmotech-acceleration-library-dev -w /opt -v $(PWD):/opt python:3.11 bash
```

```
# pip install -r requirements.txt
# pip install pytest
# pytest
```

```
$ docker container start -i cosmotech-acceleration-library-dev
```

## mobility
{id: docker-python-mobility}


* [mobility](https://github.com/mobility-team/mobility)

```
$ git clone https://github.com/mobility-team/mobility.git
$ cd mobility
```

For Windows:
CMD:

```
$ docker run -it --name mobility-dev -w /opt -v %cd%:/opt python:3.9 bash
```

PowerShell:

```
$ docker run -it --name mobility-dev -w /opt -v ${PWD}:/opt python:3.9 bash
```

For Linux:

```
$ docker run -it --name mobility-dev -w /opt -v $(PWD):/opt python:3.9 bash
```

```
# pip install -r requirements.txt && pip install -e .
# pip install pytest
# pytest
```

```
$ docker container start -i mobility-dev
```

## PHX
{id: docker-python-phx}


* [PHX](https://github.com/PH-Tools/PHX)

```
$ git clone https://github.com/PH-Tools/PHX.git
$ cd PHX
```

For Windows:
CMD:

```
$ docker run -it --name phx-dev dev -w /opt -v %cd%:/opt python:3.7 bash
```

PowerShell:

```
$ docker run -it --name phx-dev -w /opt -v ${PWD}:/opt python:3.7 bash
```

For Linux:

```
$ docker run -it --name phx-dev -w /opt -v $(PWD):/opt python:3.7 bash
```

```
# pip install -r dev-requirements.txt && pip install -e .
# pytest
```

```
$ docker container start -i phx-dev
```

## cybrid-api-id-python
{id: docker-python-cybrid-api-id-python}

* [cybrid-api-id-python](https://github.com/Cybrid-app/cybrid-api-id-python)

```
$ git clone https://github.com/Cybrid-app/cybrid-api-id-python.git
$ cd cybrid-api-id-python
```

For Windows:
CMD:

```
$ docker run -it --name cybrid-api-id-python-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:

```
$ docker run -it --name cybrid-api-id-python-dev -w /opt  -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name cybrid-api-id-python-dev -w /opt  -v $(PWD):/opt python:3.11 bash
```

```
# pip install -r requirements.txt && pip install pytest
# pytest
```

```
$ docker container start -i cybrid-api-id-python-dev
```

## pymx2
{id: docker-python-pymx2}


* [pymx2](https://github.com/vpaeder/pymx2)

```
$ git clone https://github.com/vpaeder/pymx2.git
$ cd pymx2
```

For Windows:
CMD:

```
$ docker run -it --name pymx2-dev -w /opt -v %cd%:/opt python:3.11 bash
```

PowerShell:

```
$ docker run -it --name pymx2-dev -w /opt  -v ${PWD}:/opt python:3.11 bash
```

For Linux:

```
$ docker run -it --name pymx2-dev -w /opt  -v $(PWD):/opt python:3.11 bash
# python -m setup install
```

```
# python -m unittest
```

```
$ docker container start -i pymx2-dev
```

## TOML Kit
{id: toml-kit}

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
{id: dialogy}

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

## Teiphy
{id: teiphy}

* [Teiphy](https://github.com/jjmccollum/teiphy)

Steps to run tests on a docker container:

```
git clone https://github.com/jjmccollum/teiphy.git
cd teiphy
docker run -it --name teiphy -w /opt -v$(pwd):/opt python:3.11 bash
pip install poetry
poetry install
poetry run pytest
```

## Python Automation Framework
{id: python-automation-framework}

* [python-automation-framework](https://github.com/mreiche/python-automation-framework)

Steps to run tests on a docker container:

```
git clone https://github.com/mreiche/python-automation-framework.git
cd python-automation-framework
docker run -it --name python-automation-framework -w /opt -v$(pwd):/opt python:3.11 bash
pip install pytest
pip install -r requirements.txt
PYTHONPATH="." pytest --numprocesses=4 --cov=paf test
```

## Python Bitcoinlib
{id: python-bitcoin-lib}

* [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)

Steps to run tests on a docker container:

```
git clone https://github.com/petertodd/python-bitcoinlib.git
cd python-bitcoinlib
docker run -it --name python-bitcoinlib -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover
```

## Overloaded Iterables
{id: overloaded-iterables}

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
{id: xapi-python}

* [xapi-python](https://github.com/pawelkn/xapi-python)

Steps to run tests on a docker container:

```
git clone https://github.com/pawelkn/xapi-python.git
cd xapi-python
docker run -it --name xapi-python -w /opt -v$(pwd):/opt python:3.11 bash
python3 -m unittest discover tests
```

## nats-python
{id: nats-python}

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


