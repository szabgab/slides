# R data.table


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


