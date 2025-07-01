import json
import os
import time
import sys

if len(sys.argv) != 2:
    exit("Usage: {sys.argv[0]}  NAME")

data = {
    'name': [],
    'time': [],
}
filename = 'mydata.json'

if os.path.exists(filename):
    with open(filename) as fh:
        json_str = fh.read()
        # print(json_str)
        data = json.loads(json_str)

data['name'].append(sys.argv[1])
data['time'].append(time.time())



with open(filename, 'w') as fh:
   json_str = json.dumps(data, indent=4)
   fh.write(json_str)
