import csv
import sys

def read_csv_file(filename):
    name_of = {}
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            name_of[ row['fname'] ] = row
    print(name_of)
    return name_of

filename = 'examples/csv/monty_python.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

people = read_csv_file(filename)
print(people["Graham"]["lname"])  # Champman
print(people["John"]["born"])     # 27 October 1939
print(people["Michael"])
     # {'lname': 'Palin', 'born': '5 May 1943', 'fname': 'Michael'}
print(people["Terry"]["lname"])  # Gilliam
