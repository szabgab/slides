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
}

print(data)

with open('data.json', 'w') as fh:
    json.dump(data, fh)
