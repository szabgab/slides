from collections import Counter

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

cnt = Counter()
for word in words:
   cnt[word] += 1

print(cnt)
for w in cnt.keys():
   print("{}:{}".format(w, cnt[w]))



