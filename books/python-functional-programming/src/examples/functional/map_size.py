import sys

def double(num):
    return 2 * num

numbers = [7, 2, 4, 1]

double_iterable = map(double, numbers)
double_numbers = list(map(double, numbers))

print(sys.getsizeof(double_iterable))
print(sys.getsizeof(double_numbers))
