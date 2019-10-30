import re, random

chars = ['G', 'A', 'T', 'C']
dna = ''
for i in range(100):
    dna += chars[random.randrange(4)]

print(dna)

'''
Generating regexes:

   ([GATC]{1}).*\1
   ([GATC]{2}).*\1
   ([GATC]{3}).*\1
   ([GATC]{4}).*\1
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
