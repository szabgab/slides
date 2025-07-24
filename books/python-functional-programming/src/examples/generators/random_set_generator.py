import random

def choices(values, **kw):
    while True:
        yield random.choices(values, **kw)

count = 0
for val in choices(['a', 'b', 'c', 'd', 'e', 'f'], k=2):
    print(val)
    count += 1
    if count > 10:
        break

