import yaml

filename = "data.yaml"

with open(filename) as fh:
    data = yaml.load(fh, Loader=yaml.Loader)

print(data)

