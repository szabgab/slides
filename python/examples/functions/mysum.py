def mysum(*numbers):
    print(numbers)
    print(type(numbers))
    total = 0
    for s in numbers:
        total += s
    return total

if __name__ == '__main__':
    print(mysum())
    print(mysum(1))
    print(mysum(1, 2))
    print(mysum(1, 1, 1))
