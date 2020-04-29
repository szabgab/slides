import sys

def double(n):
    print(f"double {n}")
    return 2 * n

numbers = [1, 4, 2, -1, 23, 12, 5, 6, 34, 143123, 98, 213]

double_numbers = map(double, numbers)
print(double_numbers)
for num in double_numbers:
    print(num)
    if num > 42:
        break

print()
print(sys.getsizeof(numbers))
print(sys.getsizeof(double_numbers))


