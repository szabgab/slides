val = 42

print(f"{val:b}") #  binary:    101010
print(f"{val:c}") #  character: *
print(f"{val:d}") #  decimal:   42      (default)
print(f"{val:o}") #  octal:     52
print(f"{val:x}") #  hexa:      2a
print(f"{val:X}") #  hexa:      2A
print(f"{val:n}") #  number:    42


print(f"{val}")   # 42 (same as decimal)

# Zero padding
val = 3
print(f"'{val:2n}'")  # ' 3'
print(f"'{val:02n}'") # '03'
val = 14
print(f"'{val:02n}'") # '14'


# Zero padding hexa
val = 3
print(f"'{val:2X}'")  # ' 3'
print(f"'{val:02X}'") # '03'
val = 14
print(f"'{val:02X}'") # '0E'
val = 70
print(f"'{val:02X}'") # '46'

