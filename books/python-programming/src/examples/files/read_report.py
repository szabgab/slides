import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

total = 0
with open(filename, "r") as fh:
    for row in fh:
        if "Report" not in row:
            continue
        text, value = row.split(":")
        # print(value)
        value = float(value.strip())
        # print(value)
        total += value

print(total)
