letters = 'axzb'
print(letters)         # 'axzb'
s = sorted(letters)
print(s)               # ['a', 'b', 'x', 'z']
print(letters)         # 'axzb'

r = ''.join(sorted(letters))
print(r)               # abxz

