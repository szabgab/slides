import sys
from mymath import fact

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} n k")


'''
   n         n!
   -  =   ---------
   k      k!*(n-k)!

'''

n = int(sys.argv[1])
k = int(sys.argv[2])

n_fact = fact(n)
print(n_fact)

n_k_fact = fact(n-k)
print(n_k_fact)

k_fact = fact(k)
print(k_fact)


bc = n_fact // (k_fact * n_k_fact)
print(bc)

