numbers = [1, 7, 19, 5, 57,  23, 8]

def big(x):
    print(f"filtering {x}")
    return x > 10

def double(y):
    print(f"double {y}")
    return 2*y

big_numbers = filter(big, numbers)
print(big_numbers)

doubles = map(double,  big_numbers)
print(doubles)

for num in doubles:
    print(num)
