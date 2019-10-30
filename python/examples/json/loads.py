import json

with open('examples/json/data.json') as fh:
    json_str = fh.read()

print(json_str)
b = json.loads(json_str)
print(b)
