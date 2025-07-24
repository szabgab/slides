def add(x, y):
    return x*y

print(add(2, 3))  # 6

def add(x):
    return x+x

print(add(2))  # 4

add(2, 3)
# TypeError: add() takes exactly 1 argument (2 given)

