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

## Python [dialogy](https://github.com/skit-ai/dialogy)
{id: docker-python-dialogy}

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

## Python [toml_tools](https://github.com/JamesParrott/toml_tools)
{id: docker-python-toml_tools}
Have contributors file instructions
```
git clone https://github.com/JamesParrott/toml_tools
cd toml_tools
docker run -it --name toml_tools_test -w /opt -v <working directory>\toml_tools:/opt python:3.11 bash
$ pip install --upgrade pip
$ pip install tox
$ tox -e py
```
  
  
## Python [penn](https://github.com/interactiveaudiolab/penn)
{id: docker-python-penn}
  
There is no contribution file, but there is an explanation of how to clone and run the project in the readme file. 
Added a [contribution.md](https://github.com/interactiveaudiolab/penn/pull/4) file with the following instructions:
```
git clone https://github.com/interactiveaudiolab/penn
cd penn
docker run -it --name penn_test -w /opt -v <working directory>\penn:/opt python:3.11 bash
$ pip install -r requirements.txt && pip install -e .
```

## Python [nbt-structure-utils](https://github.com/BenBenBenB/nbt-structure-utils)
{id: docker-python-nbt-structure-utils}  
 
There is no contribution file. Added a new [PR](https://github.com/BenBenBenB/nbt-structure-utils/pull/12) for contribution file with the following instructions:
```
git clone https://github.com/BenBenBenB/nbt-structure-utils
cd nbt-structure-utils
docker run -it --name nbt_test -w /opt -v <working directory>\nbt-structure-utils:/opt python:3.11 bash
$ pip install poetry
$ poetry install
```  
  

## Python [sanic-restful](https://github.com/linzhiming0826/sanic-restful)
{id: docker-python-sanic-restful}
  
There is no contribution file. Added a new [PR](https://github.com/linzhiming0826/sanic-restful/pull/10) for contribution file with the following instructions: 
```
git clone https://github.com/linzhiming0826/sanic-restful
cd sanic-restful
docker run -it --name sanic-restful_test -w /opt -v <working directory>\sanic-restful:/opt python:3.11 bash
```
  
  
