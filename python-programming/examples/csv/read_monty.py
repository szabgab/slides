import csv

file = 'examples/csv/monty_python.csv'
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        print(row)

