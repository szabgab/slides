import sys
import os
import time
import re

if len(sys.argv) <= 1:
    exit(f"Usage: {sys.argv[0]} INFILEs")

conversion = {
    'R1'  : 'R2',
    'R2'  : 'R3',
    'R3'  : 'R1',
    'R12' : 'R21',
    'R21' : 'R12',
}
#print(conversion)

def replace(mapping, files):
    regex = r'\b(' + '|'.join(mapping.keys()) + r')\b'
    #print(regex)
    ts = time.time()

    for filename in files:
        with open(filename) as fh:
            data = fh.read()
        data = re.sub(regex, lambda match: mapping[match.group(1)], data)
        os.rename(filename, f"{filename}.{ts}")       # backup with current timestamp
        with open(filename, 'w') as fh:
            fh.write(data)

replace(conversion, sys.argv[1:]);

