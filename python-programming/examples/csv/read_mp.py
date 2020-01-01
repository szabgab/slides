import csv

def read_csv_file():
    file = 'examples/csv/monty_python.csv'
    name_of = {}
    with open(file) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            name_of[ row['fname'] ] = row
    print(name_of)
    return name_of

people = read_csv_file()
print(people["Graham"]["lname"])  # Champman
print(people["John"]["born"])     # 27 October 1939
print(people["Michael"])
     # {'lname': 'Palin', 'born': '5 May 1943', 'fname': 'Michael'}
print(people["Terry"]["lname"])  # Gilliam
