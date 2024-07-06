import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]}")

filename = sys.argv[1]

with open(filename) as fh:
    rows = map(lambda s: s.rstrip("\n"), fh.readlines())

print("SIZE:", sys.getsizeof(rows))

for row in rows:
    print(row)


with open(filename) as fh:
    rows = map(lambda s: s.rstrip("\n"), fh)
    print("SIZE:", sys.getsizeof(rows))

    for row in rows:
        print(row)



#with open(filename) as fh:
#    #for row in fh:
#    #    ...
#    #rows = map(lambda s: s.rstrip("\n"), fh.readlines())
#    rows = map(lambda s: s.rstrip("\n"), fh)
#
#    for row in rows:
#        print(row)
