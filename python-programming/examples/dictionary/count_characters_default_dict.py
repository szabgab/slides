from collections import defaultdict

text = """
This is a very long text.
OK, maybe it is not that long after all.
"""

# print(text)
count = defaultdict(int)

for char in text:
    if char == '\n':
        continue
    count[char] += 1

for key in sorted( count.keys() ):
    print("'{}' {}".format(key, count[key]))
