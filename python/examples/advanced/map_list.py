def double(n):
    return 2 * n

numbers = [1, 2, 3, 4]
name = "FooBar"

double_numbers = list(map(double, numbers))
print(double_numbers)                         # [2, 4, 6, 8]

double_letters = list(map(double, name))
print(double_letters)  # ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']
