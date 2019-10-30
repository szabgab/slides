numbers = [1, 2, 3, 4]

print(reduce(lambda x,y: x+y, numbers))    # 10 = ((1+2)+3)+4
print(reduce(lambda x,y: x*y, numbers))    # 24 = ((1*2)*3)*4
print(reduce(lambda x,y: x/y, [8, 4, 2]))  # ?

print(reduce(lambda x,y: x+y, [2]))

# print(reduce(lambda x,y: x+y, []))
     # TypeError: reduce() of empty sequence with no initial value
print(reduce(lambda x,y: x+y, [], 0))
print(reduce(lambda x,y: x+y, [2,4], 1)) # 7
