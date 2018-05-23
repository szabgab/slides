import json

class Thing(object):
    def data_file():
        return "/corporate/fixed/path/data.json"

    def get_sum(self):
        data_file = self.data_file()
        with open(data_file) as fh:
            data = json.load(fh)
            # ...
            result = data['x'] + data['y']
            return result

