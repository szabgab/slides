import random

total = 0
while total < 10000000:
    print(total)
    total += random.randrange(20)

    if total % 17 == 1:
        break

    if total ** 2 % 23 == 7:
        break

print("done")
