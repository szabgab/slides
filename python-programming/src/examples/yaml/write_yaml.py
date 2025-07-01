import yaml

filename = "out.yaml"

data = {
    "name": "Foo Bar",
    "children": ["Kid1", "Kid2", "Kid3"],
    "car": None,
    "code": 42,
}


with open(filename, 'w') as fh:
    yaml.dump(data, fh, Dumper=yaml.Dumper)

