numbers = [2, 1, 4, 3]

# min
print(reduce(lambda x,y: x if x < y else y, numbers))  # 1
# max
print(reduce(lambda x,y: x if x > y else y, numbers))  # 4

# factorial
n = 4
print(reduce(lambda x,y: x*y, range(1, n+1), 1))   # 24
# The 1 at the end is the initializor of reduce to provide
# correct results for n = 0.

a = [1, 3, 6]
b = [2, 4, 5]
c = map(lambda x,y: x if x > y else y, a, b)
print(c)  # [2, 4, 6]
