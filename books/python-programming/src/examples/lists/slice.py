letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::])       # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::1])      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::2])      # ['a', 'c', 'e', 'g', 'i']

print(letters[1::2])     # ['b', 'd', 'f', 'h', 'j']

print(letters[2:8:2])    # ['c', 'e', 'g']

print(letters[1:20:3])   # ['b', 'e', 'h']

print(letters[20:30:3])   # []

print(letters[8:3:-2])   # ['i', 'g', 'e']

