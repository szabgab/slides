people = [
    {
      'fname': 'Moshe',
      'lname': 'Cohen',
      'email': 'moshe@cohen.com',
    },
    {
      'fname': 'Dana',
      'lname': 'Levy',
      'email': 'dana@levy.com',
    }
]
#print(people[0]['fname'])
#for person in people:
#    print(person)

people_by_name = {
    'Moshe Cohen': 'moshe@cohen.com',
    'Dana Levy': 'dana@levy.com',
}
#print(people_by_name['Dana Levy'])
#for name, email in people_by_name.items():
#    print(f"{name}  ->  {email}")



full_people_by_name = {
    'Moshe': {
      'fname': 'Moshe',
      'lname': 'Cohen',
      'email': 'moshe@cohen.com',
    },
    'Dana': {
      'fname': 'Dana',
      'lname': 'Levy',
      'email': 'dana@levy.com',
    }
}

print(full_people_by_name['Moshe']['lname'])
print(full_people_by_name['Dana'])
for fname, data in full_people_by_name.items():
    print(fname)
    print(data)






