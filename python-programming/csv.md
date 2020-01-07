# CSV
{id: csv}

## Reading CSV the naive way
{id: reading-csv-the-naive-way}

![](examples/csv/process_csv_file.csv)
![](examples/csv/read_csv_split.py)

**python examples/csv/read_csv_split.py examples/csv/process_csv_file.csv**



## CSV with quotes and newlines
{id: csv-with-newlines}

![](examples/csv/process_csv_file_quote.csv)
![](examples/csv/process_csv_file_newline.csv)


## Reading a CSV file
{id: reading-csv}
{i: csv}

![](examples/csv/read_csv.py)

**python examples/csv/read_csv.py examples/csv/process_csv_file.csv**



Dialects of CSV files. See also:
[csv](http://docs.python.org/3/library/csv.html)


## CSV dialects
{id: csv-dialects}

![](examples/csv/dialects.py)
![](examples/csv/dialects.out)


## CSV to dictionary
{id: csv-to-dictionary}

![](examples/csv/monty_python.csv)
![](examples/csv/read_monty.py)
![](examples/csv/read_monty.out)


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


## Solution: CSV
{id: solution-csv}

![](examples/csv/read_mp.py)



