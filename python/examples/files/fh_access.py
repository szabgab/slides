
names = ['Foo', 'Bar', 'Baz']
for name in names:
    print(name)
print(names[1])


filename = 'data/README'
with open(filename, 'r') as fh:
    for line in fh:
        print(line)

with open(filename, 'r') as fh:
    print(fh[2])
