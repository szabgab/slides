import re
import random

chars = ['G', 'A', 'T', 'C']
dna = 'AT'
for i in range(100):
    dna += random.choice(chars)

print(dna)

# finds the first one, not necessarily the longest one
match = re.search(r"([GATC]+).*\1", dna)
if match:
    print(match.group(1))

'''
Generating regexes:

   ([GATC]{1}).*\1
   ([GATC]{2}).*\1
   ([GATC]{3}).*\1
   ([GATC]{4}).*\1
   ...
'''
length = 1
result = ''
while True:
    regex = r'([GATC]{' + str(length) + r'}).*\1'
    #print(regex)
    m = re.search(regex, dna)
    if m:
        result = m.group(1)
        length += 1
    else:
        break

print(result)
print(len(result))
