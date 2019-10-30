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
for p in people:
    by_name[ p['name' ] ] = p
    by_id[ p['id' ] ] = p
print(by_name)
print(by_id)

print(by_name["Foo"])
by_name["Foo"]['email'] = 'foo@weizmann.ac.il'
print(by_name["Foo"])

print(by_id["1"])
