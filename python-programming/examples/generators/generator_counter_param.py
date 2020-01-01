def counter(n = 1):
    while(True):
        yield n
        n += 1

for c in counter():
    print(c)
    if c >= 4:
        break

for c in counter(6):
    print(c)
    if c >= 10:
        break
