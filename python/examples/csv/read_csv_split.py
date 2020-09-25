import sys, csv

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} FILENAME\n".format(sys.argv[0]))
    exit()

filename = sys.argv[1]
count = 0
with open(filename) as fh:
    for line in fh:
        line = line.rstrip("\n")
        row = line.split(';')
        #print(row)
        count += int(row[2])

print("Total: {}".format(count))
