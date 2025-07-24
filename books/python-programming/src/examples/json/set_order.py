from collections import OrderedDict
import json

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

planned_order = ('b', 'c', 'd', 'a')
e = OrderedDict(sorted(d.items(), key=lambda x: planned_order.index(x[0])))
print(e)

out = json.dumps(e, sort_keys=False, indent=4, separators=(',', ': '))
print(out)

print('-----')

# Create index to value mapping dictionary from a list of values
planned_order = ('b', 'c', 'd', 'a')
plan = dict(zip(planned_order, range(len(planned_order))))
print(plan)

f = OrderedDict(sorted(d.items(), key=lambda x: plan[x[0]]))
print(f)
out = json.dumps(f, sort_keys=False, indent=4, separators=(',', ': '))
print(out)

