files = ['examples/files/a.txt', 'examples/files/b.txt']
names = []
values = []

for filename in files:
    with open(filename) as fh:
        for line in fh:
            name, value = line.rstrip("\n").split("=")
            value = int(value)
            if name in names:
                idx = names.index(name)
                values[idx] += value
            else:
                names.append( name )
                values.append( value )

pairs = []
for ix in range(len(names)):
    pairs.append((names[ix], values[ix]))

# for name, value in zip(names, values):
#     pairs.append((name, value))

print(pairs)
print(sorted(pairs))
print(sorted(pairs, key=lambda p: p[1]))

with open('out.txt', 'w') as fh:
    for name, value in pairs:
        fh.write("{}={}\n".format(name, value))
