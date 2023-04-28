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

## Cosmo-Tech
{id: docker-python-Cosmo-Tech}


* [Cosmo-Tech](https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library)

```
$ git clone https://github.com/Cosmo-Tech/CosmoTech-Acceleration-Library.git
$ cd CosmoTech-Acceleration-Library
$ docker run -t -i --name cosmotech-acceleration-library-dev -v /opt/CosmoTech-Acceleration-Library -v /C:/Users/YourUserName/CosmoTech-Acceleration-Library:/opt python:3.11 bash

# cd opt
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
$ docker run -t -i --name mobility-dev -v /opt/mobility -v /C:/Users/YourUserName/mobility:/opt python:3.9 bash
# cd opt
# pip install -r requirements.txt && pip install -e .

# pip install pytest
# pytest
```

```
$ docker container start -i mobility-dev
```

## PHX
{id: docker-python-PHX}


* [PHX](https://github.com/PH-Tools/PHX)
```
$ git clone https://github.com/PH-Tools/PHX.git
$ cd PHX
$ docker run -it --name phx-dev -v /opt/phx -v /$(pwd):/opt python:3.7 bash
# cd opt
# pip install -r dev-requirements.txt && pip install -e . 

# pytest
```

```
$ docker container start -i start -i phx-dev
```

## cybrid-api-id-python
{id: docker-python-cybrid-api-id-python}


* [cybrid-api-id-python](https://github.com/Cybrid-app/cybrid-api-id-python)
```
$ git clone https://github.com/Cybrid-app/cybrid-api-id-python.git
$ cd cybrid-api-id-python
$ docker run -t -i --name cybrid-api-id-python-dev  -v /opt/phx -v /$(pwd):/opt python:3.11 bash
# cd opt
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
$ docker run -it --name pymx2-dev  -v /opt/pymx2 -v /$(pwd):/opt python:3.11 bash
# python -m setup install

# python -m unittest
```

```
$ docker container start -i pymx2-dev
```



