numbers = [1, 2, 3, 4]

def dbl(x):
   return 2*x
d1 = map(dbl, numbers)
print(d1)  # [2, 4, 6, 8]

double = lambda x: 2*x
d2 = map(double, numbers)
print(d2)  # [2, 4, 6, 8]

d3 = map(lambda n: 2*n, numbers)
print(d3)   # [2, 4, 6, 8]
