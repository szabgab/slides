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

with open('out.txt', 'w') as fh:
    for ix in range(len(names)):
        fh.write("{}={}\n".format(names[ix], values[ix]))
