import sys
from mymath import fact

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} n r")

'''
               n!
 P(n, r)  =  -----
             (n-r)!

'''


n = int(sys.argv[1])
r = int(sys.argv[2])

n_fact = fact(n)
#print(n_fact)

n_r_fact = fact(n-r)
#print(n_r_fact)

P = n_fact // n_r_fact
print(P)
