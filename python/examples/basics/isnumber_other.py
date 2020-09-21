val = '1'
print(val.isdecimal()) # True
print(val.isnumeric()) # True

val = '1.1'
print(val.isdecimal()) # False
print(val.isnumeric()) # False

val = '٣'  # arabic 3
print(val.isdecimal()) # True
print(val.isnumeric()) # True

val = '½' # unicode 1/2
print(val.isdecimal()) # False
print(val.isnumeric()) # True

val = '②' # unocde circled 2
print(val.isdecimal()) # False
print(val.isnumeric()) # True

