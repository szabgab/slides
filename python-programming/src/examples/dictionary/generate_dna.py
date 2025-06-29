import sys
import random

if len(sys.argv) != 2:
    exit("Need a number")
count = int(sys.argv[1])

dna = []
for _ in range(count):
    dna.append(random.choice(['A', 'C', 'T', 'G']))
print(''.join(dna))

