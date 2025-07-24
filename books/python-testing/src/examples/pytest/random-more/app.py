import random

def random_sum(n):
    total = 0
    for _ in range(n):
        current = random.randint(0, 10)
        #print(current)
        total += current
    return total

