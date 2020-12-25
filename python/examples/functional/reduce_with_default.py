from functools import reduce

print( reduce(lambda x,y: x+y, [], 0) )      # 0
print( reduce(lambda x,y: x+y, [1, 2], 0) )  # 3

print( reduce(lambda x,y: x*y, [1, 2], 0) )  # 0
print( reduce(lambda x,y: x*y, [2, 3], 1) )  # 6
print( reduce(lambda x,y: x*y, [], 0) )      # 0
