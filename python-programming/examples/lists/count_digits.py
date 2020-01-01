numbers = [1203, 1256, 312456, 98]

count = [0] * 10

for n in numbers:
    for d in str(n):
        count[int(d)] += 1

for d in range(0, 10):
    print("{}  {}".format(d, count[d]))

