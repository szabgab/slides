import sys
import re
import json


def main():
    if len(sys.argv) != 2:
        exit(f'Usage: {sys.argv[0]} FILENAME')
    dom = parse(sys.argv[1])
    print(json.dumps(dom))

def parse(filename):
    dom = []
    with open(filename) as fh:
        for line in fh:
            line = line.rstrip('\n')

            match = re.search('\A#\s+(.*?)\s*\Z', line)
            if match:
                dom.append({
                    'h1' : match.group(1)
                })
                continue

            match = re.search('\A##\s+(.*?)\s*', line)
            if match:
                dom.append({
                    'h2' : match.group(1)
                })
                continue

    return dom


if __name__ == '__main__':
    main()


