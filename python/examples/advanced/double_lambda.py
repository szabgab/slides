numbers = [1, 2, 3, 4]
name = "FooBar"


double_numbers = list( map( lambda n: n * 2, numbers) )
print(double_numbers) # [2, 4, 6, 8]


double_letters = map( lambda n: n * 2, name)
for cr in double_letters:
    print(cr)
# FF
# oo
# oo
# BB
# aa
# rr

