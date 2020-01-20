counter = {}

word = 'eggplant'

if word not in counter:
    counter[word] = 0
counter[word] += 1

print(counter)
