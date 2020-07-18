def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step


for c in count(start=19, step=1):
    print(c)
    if c > 23:
        break

