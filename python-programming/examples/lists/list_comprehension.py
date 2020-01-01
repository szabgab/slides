text = ['aaaa', 'bb', 'ccc ccc']

length_1 = map(lambda x: len(x), text)
print(length_1)       # <map object at 0x7f60ceb90f98>
print(list(length_1)) # [4, 2, 7]


length_2 = map(len, text)
print(length_2)       # <map object at 0x7f60ceb90fd0>
print(list(length_2)) # [4, 2, 7]


length_3 = [ len(s)  for s in text ]
print(length_3) # [4, 2, 7]
