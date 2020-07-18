def is_big(x):
    return x > 100

def is_even(x):
    return not x % 2

numbers = [90, 102, 101, 104]

cond = [is_big, is_even]

# z = ...
print(z) # [102, 104]
