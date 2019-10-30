# print(my_reduce()) # TypeError: my_reduce() takes at least 1 argument (0 given)
print(my_reduce(lambda x,y: x+y))             # None
print(my_reduce(lambda x,y: x+y, 3))          # 3
print(my_reduce(lambda x,y: x+y, -1, 4, -2))  # 1

print(my_reduce(lambda x,y: x*y, -1, 4, -2))  # 8
