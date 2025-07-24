from functools import reduce

numbers = [1, 2, 3, 4]

print(reduce(lambda x,y: x+y, numbers))    # 10  = ((1+2)+3)+4
print(reduce(lambda x,y: x*y, numbers))    # 24  = ((1*2)*3)*4
print(reduce(lambda x,y: x/y, [8, 4, 2]))  # 1.0 = (8/4)/2

print(reduce(lambda x,y: x+y, [2]))        # 2
print(reduce(lambda x,y: x*y, [2]))        # 2
