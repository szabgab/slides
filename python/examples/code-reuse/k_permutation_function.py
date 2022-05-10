import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} n r")

'''
               n!
 P(n, r)  =  -----
             (n-r)!

'''

def fact(x):
    x_fact = 1
    for i in range(1, x+1):
        x_fact *= i
    return x_fact


n = int(sys.argv[1])
r = int(sys.argv[2])

n_fact = fact(n)
#print(n_fact)

n_r_fact = fact(n-r)
#print(n_r_fact)

P = n_fact // n_r_fact
print(P)
