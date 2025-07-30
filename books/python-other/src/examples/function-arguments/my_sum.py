def my_sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s

print(my_sum())           # 0
print(my_sum(2, 3))       # 5
print(my_sum(-1, 2, -1,)) # 0
