text = """
This is a very long text.
OK, maybe it is not that long after all.
"""

# print text
count = {}
for c in text:
    if c == '\n':
        continue
    if c not in count:
        count[c] = 0
    count[c] += 1

for k in count:
    print("'{}' {}".format(k, count[k]))
