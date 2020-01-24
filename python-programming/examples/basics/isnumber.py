val = input("Type in a number: ")
print(val)
print(val.isdecimal())
print(val.isnumeric())

if val.isdecimal:
    num = int(val)
    print(num)
