def mysum(*numbers):
    print(numbers)
    total = 0
    for s in numbers:
        total += s
    return total

print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 1, 1))

x = [2, 3, 5, 6]

print(mysum(*x))

mysum(x)

