def double(num):
    return 2 * num

numbers = [1, 2, 3, 4]
name = "FooBar"

double_numbers = list(map(double, numbers))
print(double_numbers)

double_letters = list(map(double, name))
print(double_letters)
