
numbers = [1, 1]
for n in numbers:
    print(n)
    numbers.append(numbers[-1] + numbers[-2])

    if n > 100:
        break

print(numbers)
