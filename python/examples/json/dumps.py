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

json_str = json.dumps(a)
print(json_str)

with open('data.json', 'w') as fh:
    fh.write(json_str)
