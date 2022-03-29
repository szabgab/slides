import json

with open('data.json', 'r') as fh:
    data = json.load(fh)
print(data)
