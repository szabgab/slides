filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
    lines = fh.readlines()   # reads all the lines into a list

print(f"number of lines: {len(lines)}")

for line in lines:
    print(line, end="")
print('------')

lines.reverse()
for line in lines:
    print(line, end="")

