# CSV
{id: csv}

## Reading CSV the naive way
{id: reading-csv-the-naive-way}

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

![](examples/csv/read_csv.py)

```
python examples/csv/read_csv.py examples/csv/plain.csv
```

## CSV with newlines missing closing quote
{id: csv-with-newlines-missing-closing-quote}

![](examples/csv/with_newlines_error.csv)


## CSV to dictionary
{id: csv-to-dictionary}
{i: DictReader}

![](examples/csv/monty_python.csv)
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


## Exercise: CSV as dictionary of dictionaries
{id: exercise-csv}

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

* Write a script that given a CSV file will tell if all the rows have the same length or if some of them are different.
* Show which ones are different.


## Solution: CSV
{id: solution-csv}

![](examples/csv/read_mp_dictionary.py)

## Solution: CSV as dictionary of tuples of dictionaries
{id: solution-csv-tuples}

Create a script called **monty_python_dictionary_of_tuples.py** that given a file like the CSV file of Monty Python troupe (examples/csv/monty_python.csv),
will create a dictionary where we can look up information about them based on the first name and last name. For example:

![](examples/csv/read_mp_tuple.py)

