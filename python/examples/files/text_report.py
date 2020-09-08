import sys

if len(sys.argv) !=2:
    exit(f"Usage: {sys.argv[0]} FILENAME")
    # text_report.txt

in_file = sys.argv[1]

with open(in_file) as fh:
    for row in fh:
        row = row.rstrip("\n")
        if 'Report:' in row:
            print(row)

print('-' * 20)

with open(in_file) as fh:
    for row in fh:
        row = row.rstrip("\n")
        if row.startswith('Report:'):
            print(row)

print('-' * 20)

total = 0
with open(in_file) as fh:
    for row in fh:
        row = row.rstrip("\n")
        #if row.startswith('Report:'):
        if 'Report:' in row:
            parts = row.split(':')
            print(int(parts[1]))
            total += int(parts[1])
print(f"Total: {total}")
