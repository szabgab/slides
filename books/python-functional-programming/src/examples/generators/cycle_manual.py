def cycle(values=[]):
    my_values = []
    for v in values:
        my_values.append(v)
        yield v
    while True:
        for v in my_values:
            yield v

i = 0
for c in cycle(['A', 'B', 'C']):
    print(c)
    i += 1
    if i >= 4:
        break
