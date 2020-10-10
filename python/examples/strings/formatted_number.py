val = 42

print("{:b}".format(val)) #  binary:    101010
print("{:c}".format(val)) #  character: *
print("{:d}".format(val)) #  decimal:   42      (default)
print("{:o}".format(val)) #  octal:     52
print("{:x}".format(val)) #  hexa:      2a
print("{:X}".format(val)) #  hexa:      2A
print("{:n}".format(val)) #  number:    42


print("{}".format(val))   # 42 (same as decimal)
