import random

def miranda():
    while True:
        yield random.random()

total = 0
for val in miranda():
    print(val)
    total += val
    if total > 10:
        break
