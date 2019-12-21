import sys
import re
import json


def main():
    if len(sys.argv) != 2:
        exit(f'Usage: {sys.argv[0]} FILENAME')
    dom = parse(sys.argv[1])
    print(json.dumps(dom, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))

def parse_verbatim(line):
    global in_verbatim
    global text
    global dom

    if in_verbatim:
        if line == '```':
            dom.append({
                'verbatim': text,
            })
            text = ''
            in_verbatim = False
        else:
            text += line + '\n'
        return True

    if line == '```':
        in_verbatim = True
        return True

    return False

def parse_header(line):
    global dom
    global text
    match = re.search(r'\A(#{1,2})\s+(.*?)\s*\Z', line)
    if match:
        if text != '':
            dom.append({
                'p': text
            })
            text = ''
        h = 'h' + str( len(match.group(1)) )
        dom.append({
            h : match.group(2)
        })
        return True
    return False


def parse(filename):
    global dom
    dom = []
    with open(filename) as fh:
        global text
        global in_verbatim
        text = ''
        in_verbatim = False
        for line in fh:
            line = line.rstrip('\n')

            if parse_verbatim(line):
                continue

            if parse_header(line):
                continue

            text += line + '\n'
        if text != '':
            dom.append({
                'p': text
            })
            text = ''

    return dom


if __name__ == '__main__':
    main()


