# CSV
{id: csv}

## What is a CSV file?
{id: what-is-a-csv-file}

* CSV stands for Comma Separated Values
* A CSV file is similar to the values you might put in an Excel file. Though in Excel each cell has both a `value` and a `format` (and maybe more) attributes. A CSV file only contains values.
* A CSV file has rows and in each row there are values separated by a comma.
* In some cases the separator is some other character. e.g. a semic-colon (`;`), a pipeline (`|`) or a TAB character. (The last one is also referred to a TSV file where TSV stands for TAB Separated Values.

* There are a number of other variations, so the csv-reading and writing librariers usually provide options to handle these variations.

* Sometimes all the lines hold values. Sometimes the first line acts as the list of column-names.

## CSV file without title row
{id: csv-file-without-title-row}

* Some of the figures in Snow White in Hungarian.

![](examples/csv/snowwhite.csv)


## CSV file with header
{id: csv-file-with-header}

* This CSV file contains information about the members of the Monthy Python show.
* The first row contains the titles of the columns.

![](examples/csv/monty_python.csv)

## Read CSV file into lists
{id: read-csv-file-into-lists}

![](examples/csv/read_csv.py)

```
python examples/csv/read_csv.py  example/snowwhite.csv
```

## CSV with newlines missing closing quote
{id: csv-with-newlines-missing-closing-quote}

![](examples/csv/with_newlines_error.csv)


## CSV to dictionary
{id: csv-to-dictionary}
{i: DictReader}

![](examples/csv/read_monty.py)
![](examples/csv/read_monty.out)


## CSV Attributes
{id: csv-attributes}

* delimiter
* doublequote
* escapechar
* lineterminator
* quotechar
* quoting
* skipinitialspace
* strict

## CSV dialects
{id: csv-dialects}
{i: list_dialects}

{aside}
The csv module defines a number of "dialects", sets of attributes.
{/aside}

![](examples/csv/dialects.py)
![](examples/csv/dialects.out)

Dialects of CSV files. See also:
[csv](http://docs.python.org/library/csv.html)

## Reading CSV the naive way
{id: reading-csv-the-naive-way}
{i: split}

* This is not recommended as it will fail in some cases. See next page!

![](examples/csv/plain.csv)
![](examples/csv/read_csv_split.py)

```
python examples/csv/read_csv_split.py examples/csv/plain.csv
```


## CSV with quotes and newlines
{id: csv-with-newlines}

![](examples/csv/with_quotes.csv)
![](examples/csv/with_newlines.csv)

## Reading a CSV file
{id: reading-csv}
{i: csv}
{i: reader}

![](examples/csv/read_csv_with_semicolons.py)

```
python examples/csv/read_csv.py examples/csv/plain.csv
```


## Exercise: CSV as dictionary of dictionaries
{id: exercise-csv-dictionary}

Create a script called **monty_python_dictionary_of_dictionaries.py** that given a file like the CSV file of Monty Python troupe (examples/csv/monty_python.csv),
will create a dictionary where we can look up information about them based on the first name. For example:

![](examples/csv/read_mp_dictionary_skeleton.py)

## Exercise: CSV as dictionary of tuples of dictionaries
{id: exercise-csv-tuples}

Create a script called **monty_python_dictionary_of_tuples.py** that given a file like the CSV file of Monty Python troupe (examples/csv/monty_python.csv),
will create a dictionary where we can look up information about them based on the first name and last name. For example:

![](examples/csv/read_mp_tuple_skeleton.py)

## Exercise: count row length in csv files
{id: exercise-count-row-length-in-csv-files}

* Write a script called **csv_column_count.py** that given a CSV file will tell if all the rows have the same length or if some of them are different.
* Show which ones are different.
* Try it on `examples/csv/plain.csv` and on `examples/csv/uneven.csv`


## Solution:  CSV as dictionary of dictionaries
{id: solution-csv-dictionary}

![](examples/csv/read_mp_dictionary.py)

## Solution: CSV as dictionary of tuples of dictionaries
{id: solution-csv-tuples}

Create a script called **monty_python_dictionary_of_tuples.py** that given a file like the CSV file of Monty Python troupe (examples/csv/monty_python.csv),
will create a dictionary where we can look up information about them based on the first name and last name. For example:

![](examples/csv/read_mp_tuple.py)

## Solution: count row length in csv files
{id: solution-count-row-length-in-csv-files}

![](examples/csv/count_csv_rows.py)


