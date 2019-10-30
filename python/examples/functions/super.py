def mysum(op, *numbers):
    print(numbers)
    if op == '+':
        total = 0
    elif op == '*':
        total = 1
    else:
        raise Exception('invalid operator {}'.format(op))

    for s in numbers:
        if op == '+':
            total += s
        elif op == '*':
            total *= s

    return total

print(mysum('+', 1))
print(mysum('+', 1, 2))
print(mysum('+', 1, 1, 1))
print(mysum('*', 1, 1, 1))
