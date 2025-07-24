x, y = 1, 2
print(x)      # 1
print(y)      # 2

x, y = y, x
print(x)      # 2
print(y)      # 1

def stats(num):
    return sum(num), sum(num)/len(num), min(num), max(num)

total, average, minimum, maximum = stats([2, 3, 4])
print(total, average, minimum, maximum) # 9 3.0 2 4
