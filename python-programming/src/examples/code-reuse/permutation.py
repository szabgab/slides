import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} n")

'''
  n!
'''

n = int(sys.argv[1])

n_fact = 1
for i in range(1, n+1):
    n_fact *= i
print(n_fact)

