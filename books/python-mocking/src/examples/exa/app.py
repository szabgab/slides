import json

data_file = "/corporate/fixed/path/data.json"

def get_sum():
    with open(data_file) as fh:
        data = json.load(fh)
        # ...
        result = data['x'] + data['y']
        return result
