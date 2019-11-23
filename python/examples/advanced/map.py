def double(n):
    return 2 * n

numbers = [1, 2, 3, 4]
name = "FooBar"

double_numbers = map(double, numbers)
print(double_numbers)   # <map object at 0x7f8eb2d849e8>

double_letters = map(double, name)
print(double_letters)   # <map object at 0x7f8eb2d84cc0>

