import re

strings = [
    'apple pie',
    'banana pie',
    'apple'
]

for s in strings:
    #print(s)
    match1 = re.search(r'apple pie', s)
    match2 = re.search(r'banana pie', s)
    if match1 or match2:
        print('Matched in', s)
