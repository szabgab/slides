
numbers = [1, 2, 3, 4]
for n in numbers[:]:
    print(n)
    if n == 2:
        numbers.remove(2)


print(numbers)
