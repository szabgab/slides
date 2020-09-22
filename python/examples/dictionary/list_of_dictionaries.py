import sys

filename = 'examples/csv/monty_python.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

people = []

with open(filename) as fh:
    fh.readline()  # skip first row
    for line in fh:
        line = line.rstrip('\n')
        fname, lname, born = line.split(',')
        people.append({
            'fname': fname,
            'lname': lname,
            'born': born,
        })

print(people[1]['fname'])
