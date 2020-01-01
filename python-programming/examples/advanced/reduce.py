from functools import reduce

numbers = [1, 2, 3, 4]

print(reduce(lambda x,y: x+y, numbers))    # 10 = ((1+2)+3)+4
print(reduce(lambda x,y: x*y, numbers))    # 24 = ((1*2)*3)*4
print(reduce(lambda x,y: x/y, [8, 4, 2]))  # 1.0

print(reduce(lambda x,y: x+y, [2]))        # 2

# print(reduce(lambda x,y: x+y, []))
    # TypeError: reduce() of empty sequence with no initial value
print(reduce(lambda x,y: x+y, [], 0))
print(reduce(lambda x,y: x+y, [2,4], 1))   # 7

mysum = 0
for num in numbers:
    mysum += num
print(mysum)         # 10

mymultiple = 1
for num in numbers:
    mymultiple *= num
print(mymultiple)    #24


