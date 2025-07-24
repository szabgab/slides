import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 4])
print(a)
print(b)
print()

print(a*b)
print(b*a)
print()

print(np.multiply(a, b))

print()
print( np.dot(a, b) )
print( np.matmul(a, b) )


