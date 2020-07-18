lines = [
    'grape banana mango',
    'nut orange peach',
    'apple nut banana apple mango',
]

one_line = ' '.join(lines)
print(one_line)
fruits = one_line.split()
print(fruits)

unique_fruits = []
for word in fruits:
    if word not in unique_fruits:
        unique_fruits.append(word)
print(sorted(unique_fruits))


# a simpler way using a set, but we have not learned sets yet.
unique = sorted(set(fruits))
print(unique)
