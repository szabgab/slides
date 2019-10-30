import re

strings = [
    'abc',
    'text: #q#',
    'str: #a#',
    'text #b# more text',
    '#a  and this? #c#',
    '#a  and this? # c#',
    '#@#',
    '#.#',
    '# #',
    '##'
    '###'
]

for s in strings:
    print('str:  ', s)
    match = re.search(r'#.#', s)
    if match:
        print('match:', match.group(0))
