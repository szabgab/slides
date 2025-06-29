import sys
import csv

filename = 'examples/csv/monty_python.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

people = {}

with open(filename) as fh:
    reader = csv.DictReader(fh)
    for line in reader:
        people[(line['fname'], line['lname'])] = line

print(people[('Eric', 'Idle')]['born'])

