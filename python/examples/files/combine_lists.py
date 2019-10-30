a_names = []
a_values = []
with open('examples/files/a.txt') as fh:
    for line in fh:
        k, v = line.rstrip("\n").split("=")
        a_names.append(k)
        a_values.append(int(v))

b_names = []
b_values = []
with open('examples/files/b.txt') as fh:
    for line in fh:
        k, v = line.rstrip("\n").split("=")
        b_names.append(k)
        b_values.append(int(v))

c_names = []
c_values = []

for i in range(len(a_names)):
    if a_names[i] in c_names:
        j = c_names.index(a_names[i])
        c_values[j] += a_values[i]
    else:
        c_names.append( a_names[i] )
        c_values.append( a_values[i] )

for i in range(len(b_names)):
    if b_names[i] in c_names:
        j = c_names.index(b_names[i])
        c_values[j] += b_values[i]
    else:
        c_names.append( b_names[i] )
        c_values.append( b_values[i] )


with open('out.txt', 'w') as fh:
    for i in range(len(c_names)):
        fh.write("{}={}\n".format(c_names[i], c_values[i]))
