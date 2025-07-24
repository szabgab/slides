from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print(d)
d.move_to_end('a')

print(d)
d.move_to_end('d', last=False)

print(d)

for key in d.keys():
    print(key)
