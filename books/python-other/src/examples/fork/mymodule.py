import random

def calc(num):
    random.seed(num)
    total = 0
    for _ in range(10000000):
        total += random.random()
    return total
