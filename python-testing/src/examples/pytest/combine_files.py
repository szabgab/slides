c = {}
with open('examples/files/a.txt') as fh:
    for line in fh:
        k, v = line.rstrip("\n").split("=")
        if k in c:
            c[k] += int(v)
        else:
            c[k] = int(v)

with open('examples/files/b.txt') as fh:
    for line in fh:
        k, v = line.rstrip("\n").split("=")
        if k in c:
            c[k] += int(v)
        else:
            c[k] = int(v)


with open('out.txt', 'w') as fh:
    for k in sorted(c.keys()):
        fh.write("{}={}\n".format(k, c[k]))
