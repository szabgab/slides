numbers = [1, 2, 3]

def update(x):
    x[0] = 23

def change(y):
    y = [5, 6]
    return y

def replace_content(z):
    z[:] = [7, 8]
    return z


print(numbers)         # [1, 2, 3]

update(numbers)
print(numbers)         # [23, 2, 3]

print(change(numbers)) # [5, 6]
print(numbers)         # [23, 2, 3]


print(replace_content(numbers)) # [7, 8]
print(numbers)                  # [7, 8]
