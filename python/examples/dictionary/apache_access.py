filename = 'examples/apache_access.log'

count = {}

with open(filename) as fh:
    for line in fh:
        space = line.index(' ')
        ip = line[0:space]
        if ip in count:
            count[ip] += 1
        else:
            count[ip] = 1

for ip in count:
    print("{:16} {:>3}".format(ip, count[ip]))

