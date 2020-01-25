def counter(n = 1):
    while True:
        yield n
        n += 1

for c in counter():
    print(c)
    if c >= 4:
        break
print('')

for c in counter(8):
    print(c)
    if c >= 12:
        break
