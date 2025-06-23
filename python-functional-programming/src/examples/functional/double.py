def double(n):
    return 2 * n

numbers = [1, 2, 3, 4]

double_numbers = []
for num in numbers:
    double_numbers.append( double(num) )
print(double_numbers)
