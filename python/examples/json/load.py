import json

with open('examples/json/data.json', 'r') as fh:
    a = json.load(fh)
print(a)
