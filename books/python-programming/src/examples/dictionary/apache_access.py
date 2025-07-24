from collections import defaultdict
import sys

filename = 'apache_access.log'
if len(sys.argv) > 1:
    filename = sys.argv[1]

count = defaultdict(int)

with open(filename) as fh:
    for line in fh:
        space = line.index(' ')
        ip = line[0:space]
        count[ip] += 1

for ip in count:
    print("{:16} {:>3}".format(ip, count[ip]))

