import json

a = {
  "fname" : 'Foo',
  "lname" : 'Bar',
  "email" : None,
  "children" : [
     "Moo",
     "Koo",
     "Roo"
  ]
}

print(a)

with open('data.json', 'w') as fh:
    json.dump(a, fh)
