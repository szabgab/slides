import sys, csv

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} FILENAME\n".format(sys.argv[0]))
    exit()

file = sys.argv[1]
fh = open(file, 'rb')

count = 0
for line in fh:
    line = line.rstrip("\n")
    row = line.split(';')
    print(row)
    count += int(row[2])

print("Total: {}".format(count))
