numbers  = [0, 1, 2, 3]

s = map(lambda n: n*n, numbers)
print(s)         # <map object at 0x7fdcab2f5940>
print(list(s))   # [0, 1, 4, 9]


squares = [n*n for n in numbers]
print(squares)   # [0, 1, 4, 9]
