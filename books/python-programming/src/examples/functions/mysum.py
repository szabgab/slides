def mysum(*numbers):
    print(numbers)
    print(type(numbers))
    total = 0
    for s in numbers:
        total += s
    return total

