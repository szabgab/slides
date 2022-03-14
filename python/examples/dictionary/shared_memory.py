people = [
    {
       "name" : "Foo",
       "id"   : "1",
    },
    {
       "name" : "Bar",
       "id"   : "2",
    },
    {
       "name" : "Moo",
       "id"   : "3",
    },
]

by_name = {}
by_id = {}
for person in people:
    by_name[ person['name' ] ] = person
    by_id[ person['id' ] ] = person
print(by_name)
print(by_id)
print('-------------------')

print(by_name["Foo"])
by_name["Foo"]['email'] = 'foo@weizmann.ac.il'

people[0]["name"] = "Foooooo";
print(by_name)
print(by_id)

print(by_name["Foo"])  # the key remained Foo !!!!
print(by_id["1"])
