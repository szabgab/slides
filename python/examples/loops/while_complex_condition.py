import random
random.seed(0) # used so we can verify the results in the next example

total = 0
while (total < 10000000) and (total % 17 != 1) and (total ** 2 % 23 != 7):
    print(total)
    total += random.randrange(20)

    # do the real work here

print("done")

