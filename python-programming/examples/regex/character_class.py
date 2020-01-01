import re

strings = [
    'abc',
    'text: #q#',
    'str: #a#',
    'text #b# more text',
    '#ab#',
    '#@#',
    '#.#',
    '# #',
    '##'
    '###'
]


for s in strings:
    print('str:  ', s)
    match = re.search(r'#[abcdef@.]#', s)
    if match:
        print('match:', match.group(0))
