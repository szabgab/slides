from collections import defaultdict

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

dd = defaultdict(lambda : 0)
for word in words:
   dd[word] += 1

print(dd)
for word in dd.keys():
   print("{}:{}".format(word, dd[word]))

