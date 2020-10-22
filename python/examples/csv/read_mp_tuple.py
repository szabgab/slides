import csv
import sys

def read_csv_file(filename):
    name_of = {}
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            name_of[ (row['fname'], row['lname']) ] = row
    return name_of

filename = 'examples/csv/monty_python.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

people = read_csv_file(filename)
#print(people)

print(people[("Graham", "Chapman")])
  # {'fname': 'Graham', 'lname': 'Chapman', 'born': '8 January 1941'}

print(people[("Michael", "Palin")])
  # {'fname': 'Michael', 'lname': 'Palin', 'born': '5 May 1943'}
