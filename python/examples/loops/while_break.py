import random
random.seed(0) # used so we can compare the results

total = 0
while total < 10000000:
    if total % 17 == 1:
        break

    if total ** 2 % 23 == 7:
        break

    print(total)
    total += random.randrange(20)

    # do the real work here

print("done")
