import json

def read(filename):
    with open(filename) as fh:
        return json.load(fh)

def save(filename, data):
    with open(filename, 'w') as fh:
        return json.dump(data, fh)
