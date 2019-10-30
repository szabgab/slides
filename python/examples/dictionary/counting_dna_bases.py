seq = "ACTNGTGCTYGATRGTAGCYXGTN"
count = {}
for c in seq:
   if c not in count:
       count[c] = 0
   count[c] += 1

for c in sorted(count.keys()):
    print("{} {} - {:>5.2f} %".format(c, count[c], 100 * count[c]/len(seq)))

# >5 is the right alignment of 5 places
# .2f is the floating point with 2 digits after the floating point
