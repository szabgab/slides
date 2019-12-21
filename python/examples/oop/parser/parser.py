import sys
import re
import json


def main():
    if len(sys.argv) != 2:
        exit(f'Usage: {sys.argv[0]} FILENAME')
    dom = parse(sys.argv[1])
    print(json.dumps(dom, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))

def parse(filename):
    dom = []
    with open(filename) as fh:
        text = ''
        for line in fh:
            line = line.rstrip('\n')

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
                continue

            text += line + '\n'

    return dom


if __name__ == '__main__':
    main()


