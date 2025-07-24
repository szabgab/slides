def double(n):
    return 2 * n

numbers = [7, 2, 4, 1]

double_iterable = map(double, numbers)
print(double_iterable)
for num in double_iterable:
    print(num)

