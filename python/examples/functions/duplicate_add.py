def add(x, y):
    return x*y

def add(x):
    return x+x

print(add(2))  # 4

add(2, 3)
# TypeError: add() takes exactly 1 argument (2 given)


