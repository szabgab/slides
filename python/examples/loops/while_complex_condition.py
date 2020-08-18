import random
random.seed(0)

total = 0
while (total < 10000000) and (total % 17 != 1) and (total ** 2 % 23 != 7):
    print(total)
    total += random.randrange(20)

print("done")

