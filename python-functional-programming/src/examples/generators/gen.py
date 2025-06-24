import sys

def my_range(limit = 1):
    n = 0
    while n < limit:
        yield n
        n += 1

for i in my_range(5):
    print(i)
print()

print(sum(my_range(10)))
print()

x = my_range(10000)
print(x)
print(sys.getsizeof(x))
