import json

data = {
  "fname" : 'Foo',
  "lname" : 'Bar',
  "email" : None,
  "children" : [
     "Moo",
     "Koo",
     "Roo",
  ],
  "fixed": ("a", "b"),
}
print(data)

json_str = json.dumps(data)
print(json_str)

with open('data.json', 'w') as fh:
    fh.write(json_str)
