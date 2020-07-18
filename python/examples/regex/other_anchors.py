import re

strings = [
    "123-XYZ-456",
    "a 123-XYZ-456 b",
    "a 123-XYZ-456",
    "123-XYZ-456 b",
    "123-XYZ-456\n",
]

regexes = [
    r'\d{3}-\w+-\d{3}',
    r'^\d{3}-\w+-\d{3}',
    r'\d{3}-\w+-\d{3}$',
    r'^\d{3}-\w+-\d{3}$',
    r'^\d{3}-\w+-\d{3}\Z',
    r'\A\d{3}-\w+-\d{3}\Z',
]

for r in regexes:
    print(r)
    for s in strings:
        #print(r, s)
        if (re.search(r, s)):
            print('   ', s)
    print('-' * 10)
