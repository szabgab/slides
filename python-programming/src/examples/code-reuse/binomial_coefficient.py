import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} n k")

'''
   n         n!
   -  =   ---------
   k      k!*(n-k)!

'''

n = int(sys.argv[1])
k = int(sys.argv[2])

n_fact = 1
for i in range(1, n+1):
    n_fact *= i
print(n_fact)

n_k_fact = 1
for i in range(1, n-k+1):
    n_k_fact *= i
print(n_k_fact)

k_fact = 1
for i in range(1, k+1):
    k_fact *= i
print(k_fact)


bc = n_fact // (k_fact * n_k_fact)
print(bc)

