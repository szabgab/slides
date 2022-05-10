import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} n")

'''
  n!
'''

n = int(sys.argv[1])

def fact(x):
    x_fact = 1
    for i in range(1, x+1):
        x_fact *= i
    return x_fact


n_fact = fact(n)
print(n_fact)

