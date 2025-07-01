import json

with open('data.json') as fh:
    json_str = fh.read()

print(json_str)
data = json.loads(json_str)
print(data)
