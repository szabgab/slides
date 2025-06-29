import sys

file_a = sys.argv[1]
file_b = sys.argv[2]

with open(file_a) as fha:
    with open(file_b) as fhb:
        line_a = None
        line_b = None
        while True:
            if line_a is None:
                line_a = fha.readline()
            if line_b is None:
                line_b = fhb.readline()

            if line_a == '' and line_b == '':
                break

            if line_a == '':
                print(line_b, end='')
                line_b = None
                continue

            if line_b == '':
                print(line_a, end='')
                line_a = None
                continue

            time_a = line_a.split(',')[0]
            time_b = line_b.split(',')[0]
            if int(time_a) < int(time_b):
                print(line_a, end='')
                line_a = fha.readline()
            else:
                print(line_b, end='')
                line_b = fhb.readline()

