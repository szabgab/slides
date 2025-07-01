import json
import sys
import os

filename = 'counter.json'

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " COUNTER")
    exit()

counter = {}

if os.path.exists(filename):
    with open(filename) as fh:
        json_str = fh.read()
        counter = json.loads(json_str)

name = sys.argv[1]
if name in counter:
    counter[name] += 1
else:
    counter[name] = 1

print(counter[name])


with open(filename, 'w') as fh:
    json_str = json.dumps(counter)
    fh.write(json_str)
