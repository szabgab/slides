from collections import defaultdict

seq = "ACTNGTGCTYGATRGTAGCYXGTN"

count = defaultdict(int)

for cr in seq:
   count[cr] += 1

for cr in sorted(count.keys()):
    print("{} {} - {:>5.2f} %".format(cr, count[cr], 100 * count[cr]/len(seq)))

# >5 is the right alignment of 5 places
# .2f is the floating point with 2 digits after the floating point
