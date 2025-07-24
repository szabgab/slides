def add(x, y):
    return x * y

for x, y, z in [(2, 2, 4), (9, 2, 11), (2, 3, 5)]:
    print(f"add({x}, {y}) == {z}")
    assert add(x, y) == z
