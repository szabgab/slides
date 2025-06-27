val = '11'
print(val.isdecimal()) # True
print(val.isnumeric()) # True

val = '1.1'
print(val.isdecimal()) # False
print(val.isnumeric()) # False

val = '٣'  # arabic 3
print(val.isdecimal()) # True
print(val.isnumeric()) # True
print(val)
print(int(val))  # 3

val = '½' # unicode 1/2
print(val.isdecimal()) # False
print(val.isnumeric()) # True
# print(float(val))  # ValueError: could not convert string to float: '½'

val = '②' # unicode circled 2
print(val.isdecimal()) # False
print(val.isnumeric()) # True
# print(int(val)) # ValueError: invalid literal for int() with base 10: '②'

