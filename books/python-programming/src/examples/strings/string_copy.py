text = "abcd"
print(text)     # abcd

text = text + "ef"
print(text)     # abcdef

other = text
print(other)     # abcdef
text = "xyz"
print(text)     # xyz
print(other)     # abcdef
