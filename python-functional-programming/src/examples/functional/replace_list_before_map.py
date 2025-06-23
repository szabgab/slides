def double(n):
    return 2 * n

numbers = [1, 4, 2]

double_numbers = map(double, numbers)

numbers = [3, 7]
for num in double_numbers:
    print(num)
