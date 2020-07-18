text = """
This is a very long text.
OK, maybe it is not that long after all.
"""

# print(text)
count = {}

for char in text:
    if char == '\n':
        continue
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

for key in sorted( count.keys() ):
    print("'{}' {}".format(key, count[key]))
