import itertools

i = 0
for c in itertools.cycle(['A', 'B', 'C']):
    print(c)
    i += 1
    if i >= 5: break

# A
# B
# C
# A
# B
