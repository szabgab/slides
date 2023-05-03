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
## Renormalizer
https://github.com/shuaigroup/Renormalizer

$ git clone https://github.com/shuaigroup/Renormalizer.git
$ cd Renormalizer
$ docker run -it --name Renormalizer-dev -w /opt -v %cd%:/opt python:latest bash
$ pip install renormalizer
$ pip install --upgrade pip
$ pip install qutip
$ pip install recommonmark
$ pip install Yaml8
$ pip install -r requirements.txt
$ pytest


