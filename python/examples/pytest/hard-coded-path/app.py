import json

data_file = "/corporate/fixed/path/data.json"

def do_something():
    with open(data_file) as fh:
        data = json.load(fh)
        # ...

