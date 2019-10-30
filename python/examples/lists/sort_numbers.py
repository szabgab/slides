numbers = [7, 2, -4, 19, 8]
print(numbers)                      # [7, 2, -4, 19, 8]
numbers.sort()
print(numbers)                      # [-4, 2, 7, 8, 19]

numbers.sort(reverse=True)
print(numbers)                      # [19, 9, 7, 2, -4]

numbers.sort(key=abs, reverse=True)
print(numbers)                      # [19, 9, 7, -4, 2]
