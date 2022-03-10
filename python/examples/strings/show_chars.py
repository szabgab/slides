import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} START END")

start, end = sys.argv[1:]
for decimal in range(int(start), int(end)+1):
    print(f"{decimal} {chr(decimal)}")
