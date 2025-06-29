import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} n r")

'''
               n!
 P(n, r)  =  -----
             (n-r)!

'''

n = int(sys.argv[1])
r = int(sys.argv[2])

n_fact = 1
for i in range(1, n+1):
    n_fact *= i
#print(n_fact)

n_r_fact = 1
for i in range(1, n-r+1):
    n_r_fact *= i
#print(n_r_fact)

P = n_fact // n_r_fact
print(P)
