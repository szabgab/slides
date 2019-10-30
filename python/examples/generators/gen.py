import sys

def my_xrange(limit = 1):
    n = 0
    while(n < limit):
        yield n
        n += 1

for i in my_xrange(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9
print()

print(sum(my_xrange(6))) # 15
print()

x = my_xrange(10000)
print(x)  # <generator object my_xrange at 0x10df71780>
print(sys.getsizeof(x))  # 80
