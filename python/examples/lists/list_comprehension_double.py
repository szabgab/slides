def double(n):
    return 2*n

numbers = [1, 2, 3, 4]
name = "FooBar"

double_numbers = [double(n) for n in numbers]
print(double_numbers) # [2, 4, 6, 8]


double_chars = [double(n) for n in name]
print(double_chars)   # ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']
