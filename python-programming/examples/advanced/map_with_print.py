def double(n):
    print(f"double {n}")
    return 2 * n

numbers = [1, 4, 2, -1]

double_numbers = map(double, numbers)
print(double_numbers)   # <map object at 0x7f8eb2d849e8>
for num in double_numbers:
    print(num)

