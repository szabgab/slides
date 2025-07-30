filename = 'examples/csv/monty_python.csv'
people = read_csv_file(filename)
#print(people)

print(people[("Graham", "Chapman")])
  # {'fname': 'Graham', 'lname': 'Chapman', 'born': '8 January 1941'}

print(people[("Michael", "Palin")])
  # {'fname': 'Michael', 'lname': 'Palin', 'born': '5 May 1943'}
