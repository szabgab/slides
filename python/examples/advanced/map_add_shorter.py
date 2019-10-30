v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8, 10]

print(map(lambda x,y: x+y, v1, v2))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
