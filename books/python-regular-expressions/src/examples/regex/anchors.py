import re

lines = [
    "text with cat in the middle",
    "cat with dog",
    "dog with cat",
]

for line in lines:
    if re.search(r'cat', line):
        print(line)


print("---")
for line in lines:
    if re.search(r'^cat', line):
        print(line)

print("---")
for line in lines:
    if re.search(r'\Acat', line):
        print(line)

print("---")
for line in lines:
    if re.search(r'cat$', line):
        print(line)

print("---")
for line in lines:
    if re.search(r'cat\Z', line):
        print(line)

