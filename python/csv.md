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

![](examples/csv/read_csv.py)

```
python examples/csv/read_csv.py examples/csv/plain.csv
```

## CSV to dictionary
{id: csv-to-dictionary}

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


## Exercise: CSV
{id: exercise-csv}

Given the CSV file of Monty Python troupe, create a dictionary where we can look up information
about them based on the first name. For example:

```
people = read_csv_file()
print(people["Graham"]["lname"])  # Champman
print(people["John"]["born"])     # 27 October 1939
print(people["Michael"])
     # {'lname': 'Palin', 'born': '5 May 1943', 'fname': 'Michael'}
print(people["Terry"]["lname"])  # Gilliam
```

For extra bonus create another dictionary where we can look up the information based on their fname and lname.

## Exercise: count row length in csv files
{id: exercise-count-row-length-in-csv-files}

* Write a script that given a CSV file will tell if all the rows have the same length or if some of them are different.
* Show which ones are different.


## Solution: CSV
{id: solution-csv}

![](examples/csv/read_mp.py)



