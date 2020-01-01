import re

filename = "phone.txt"
with open(filename) as fh:
    for line in fh:
        match = re.search(r'''\b
            (
                \d\d-\d{7}
                |
                \d\d\d-\d-\d{7}
                |
                \d\d-\d\d\d-\d\d\d\d
            )\b''', line, re.VERBOSE)
        if match:
            print(match.group(1))

