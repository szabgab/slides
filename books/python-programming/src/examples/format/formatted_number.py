val = 42

print("{:b}".format(val)) #  binary:    101010
print("{:c}".format(val)) #  character: *
print("{:d}".format(val)) #  decimal:   42      (default)
print("{:o}".format(val)) #  octal:     52
print("{:x}".format(val)) #  hexa:      2a
print("{:X}".format(val)) #  hexa:      2A
print("{:n}".format(val)) #  number:    42


print("{}".format(val))   # 42 (same as decimal)


# Zero padding
print("'{:2n}'".format(3))  # ' 3'
print("'{:02n}'".format(3)) # '03'
print("'{:02n}'".format(14)) # '14'


# Zero padding hexa
print("'{:2X}'".format(3))  # ' 3'
print("'{:02X}'".format(3)) # '03'
print("'{:02X}'".format(14)) # '0E'
print("'{:02X}'".format(70)) # '46'

