import sys
import re

def parse():
    if len(sys.argv) != 2:
        exit("Usage: {} FILEAME".format(sys.argv[0]))
    filename = sys.argv[1]
    data = {}
    # print("Dealing with " + filename)
    with open(filename) as fh:
        section = '__DEFAULT__'
        for line in fh:
            if re.match(r'^\s*(#.*)?$', line):
                continue
            m = re.match(r'^\[([^\]]+)\]\s*$', line)
            if (m):
                # print('Section "{}"'.format(m.group(1)))
                section = m.group(1)
                continue
            m = re.match(r'^\s*(.+?)\s*=\s*(.*?)\s*$', line)
            if m:
                # print 'field :"{}"  value: "{}"'.format(m.group(1), m.group(2))
                if not data.get(section):
                    data[section] = {}
                data[section][ m.group(1) ] = m.group(2)

    return data

ini = parse()
print(ini)

