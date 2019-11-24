numbers  = [0, 1, 2, 3]

gn = (n*n for n in numbers)
print(gn)   # <generator object <genexpr> at 0x7f9903dbc930>
print(list(gn)) # [0, 1, 4, 9]
