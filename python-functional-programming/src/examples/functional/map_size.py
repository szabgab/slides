import sys

def double(num):
    return 2 * num

numbers = [1, 2, 3, 4]

double_iterable = map(double, numbers)
double_numbers = list(map(double, numbers))

print(sys.getsizeof(double_numbers))  # 112
print(sys.getsizeof(double_iterable)) # 48
