text = ['aaaa', 'bb', 'ccc ccc']

length_1 = [ len(s) for s in text ]
print(length_1) # [4, 2, 7]


length_2 = [ len(s) for x in text ]
print(length_2)  # [7, 7, 7]


