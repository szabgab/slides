# Packages
{id: packages}

## CRAN
{id: cran}

* [CRAN](https://cran.r-project.org/) - The Comprehensive R Archive Network

## Install CRAN packages
{id: install-cran-packages}


```
$ R
> install.packages("csv", "lib")
```

This will install the "csv" package in the "lib" folder. It will also install all the dependencies.

## Install CRAN packages from the command line
{id: install-cran-packages-from-the-command-line}

```
Rscript -e 'install.packages("RUnit")'
```


## Read CSV file
{id: read-csv-file}

* [csv](https://www.rdocumentation.org/packages/csv/)

![](examples/csv/read_csv.R)

## Read JSON file
{id: read-json-file}
{i: JSON}
{i: read_json}

* [jsonlite](https://www.rdocumentation.org/packages/jsonlite/)

![](examples/json/read_json.R)

