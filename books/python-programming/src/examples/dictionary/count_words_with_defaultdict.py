from collections import defaultdict

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

counter = defaultdict(int)
for word in words:
   counter[word] += 1

print(counter)
for word in counter.keys():
   print("{}:{}".format(word, counter[word]))

