from collections import defaultdict

counter = defaultdict(int)

word = 'eggplant'

counter[word] += 1

print(counter)
