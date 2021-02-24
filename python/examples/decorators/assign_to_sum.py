numbers = [2, 4, 3, 1, 1, 1]
print(sum(numbers))   # 12
print(max(numbers))   #  4

sum = max
print(sum(numbers))   #  4
print(max(numbers))   #  4


sum = lambda values: len(values)
print(sum(numbers))   # 6
