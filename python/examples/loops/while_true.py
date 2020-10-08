import random
random.seed(0)

total = 0
while True:
    print(total)
    total += random.randrange(20)

    if total >= 10000000:
        break

    if total % 17 == 1:
        break

    if total ** 2 % 23 == 7:
        break

    # do the real work here

print("done")
