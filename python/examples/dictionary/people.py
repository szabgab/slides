from person import person_1, person_2

people = [person_1, person_2]
print(people[0]['fname'])
for person in people:
    print(person)
print('----------------')

people_by_name = {
    'Moshe Cohen': 'moshe@cohen.com',
    'Dana Levy': 'dana@levy.com',
}
print(people_by_name['Dana Levy'])
for name, email in people_by_name.items():
    print(f"{name}  ->  {email}")
print('----------------')



full_people_by_name = {
    'Moshe': person_1,
    'Dana': person_2,
}

print(full_people_by_name['Moshe']['lname'])
print(full_people_by_name['Dana'])
for fname, data in full_people_by_name.items():
    print(fname)
    print(data)
