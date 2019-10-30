import sys

def mysum(*numbers):
    print(numbers)
    total = 0
    for s in numbers:
        total += s
    return total

v = [int(x) for x in sys.argv[1:] ]
r = mysum( *v )
print(r)
