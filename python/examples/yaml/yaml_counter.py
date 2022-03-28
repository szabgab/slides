import sys
import os
import yaml

filename = "counter.yaml"

if len(sys.argv) > 2:
    exit(f"Usage: {sys.argv[0]} [NAME]")


counter = {}
if os.path.exists(filename):
    with open(filename) as fh:
        counter = yaml.load(fh, Loader=yaml.Loader)



if len(sys.argv) == 1:
    if counter:
        for key, value in counter.items:
            print("{key} {value}")
    else:
        print("No counters were found")
    exit()

name = sys.argv[1]

if name not in counter:
    counter[name] = 0
counter[name] += 1
print(counter[name])

with open(filename, 'w') as fh:
    yaml.dump(counter, fh, Dumper=yaml.Dumper)

