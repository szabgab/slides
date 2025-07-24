import itertools

ix = 0
for c in itertools.cycle(['A', 'B', 'C']):
    print(c)
    ix += 1
    if ix >= 5:
        break

print('')

ix = 0
for c in itertools.cycle('DEF'):
    print(c)
    ix += 1
    if ix >= 5:
        break

