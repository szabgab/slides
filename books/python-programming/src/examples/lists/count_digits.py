numbers = [1203, 1256, 312456, 98]

count = [0] * 10 # same as [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in numbers:
    for char in str(num):
        count[int(char)] += 1

for d in range(0, 10):
    print("{}  {}".format(d, count[d]))

