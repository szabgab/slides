import sys
from mymath import fact

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} n")

'''
  n!
'''

n = int(sys.argv[1])


n_fact = fact(n)
print(n_fact)

