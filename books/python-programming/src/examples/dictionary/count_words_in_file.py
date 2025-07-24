from collections import defaultdict
import sys

filename = 'README'
if len(sys.argv) > 1:
    filename = sys.argv[1]
print(filename)

count = defaultdict(int)

with open(filename) as fh:
    for full_line in fh:
        line = full_line.rstrip('\n')
        line = line.lower()
        for word in line.split():
            if word == '':
                continue
            count[word] += 1

for word in sorted(count):
    print("{:13} {:>2}".format(word, count[word]))

