import sys

numbers = xrange(10000)
print('size of numbers  :', sys.getsizeof(numbers))  # 40

# list comprehension
n1 = [ n*n for n in numbers if n % 2 ]
print('size of n1       :', sys.getsizeof(n1))  # 43048

# generator expression
n2 = ( n*n for n in numbers if n % 2 )
print('size of n2       :', sys.getsizeof(n2))   # 80
