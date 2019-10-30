import json
import os
import time

data = {}
filename = 'mydata.json'

if os.path.exists(filename):
    with open(filename) as fh:
        json_str = fh.read()
        print(json_str)
        data = json.loads(json_str)

data['name'] = 'Foo Bar'
data['time'] = time.time()


with open(filename, 'w') as fh:
   json_str = json.dumps(data)
   fh.write(json_str)
