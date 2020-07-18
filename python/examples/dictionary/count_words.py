words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

counter = {}
for word in words:
   if word not in counter:
       counter[word] = 0
   counter[word] += 1

for word in counter:
   print("{}:{}".format(word, counter[word]))



