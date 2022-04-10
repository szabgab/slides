letters = 'axzb'
print(letters)         # 'axzb'

srt = sorted(letters)
print(srt)             # ['a', 'b', 'x', 'z']
print(letters)         # 'axzb'

rev = ''.join(srt)
print(rev)               # abxz

# in one statement:
rev = ''.join(sorted(letters))
print(rev)               # abxz

