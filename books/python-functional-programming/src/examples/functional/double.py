def double(n):
    return 2 * n

numbers = [7, 2, 4, 1]

double_numbers = []
for num in numbers:
    double_numbers.append( double(num) )
print(double_numbers)
