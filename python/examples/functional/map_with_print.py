def double(n):
    print(f"double {n}")
    return 2 * n

numbers = [1, 4, 2, -1]

double_numbers = map(double, numbers)
print(double_numbers)

for num in double_numbers:
    print(num)

