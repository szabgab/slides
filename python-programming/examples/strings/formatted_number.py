x = 42

print("{:b}".format(x)) #  binary:    101010
print("{:c}".format(x)) #  character: *
print("{:d}".format(x)) #  decimal:   42      (default)
print("{:o}".format(x)) #  octal:     52
print("{:x}".format(x)) #  hexa:      2a
print("{:X}".format(x)) #  hexa:      2A
print("{:n}".format(x)) #  number:    42


print("{}".format(x))   # defaults to decimal
