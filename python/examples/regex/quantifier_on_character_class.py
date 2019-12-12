import re

strings = (
    "-a-",
    "-b-",
    "-x-",
    "-aa-",
    "-ab-",
    "--",
)

for line in strings:
    match = re.search(r'-[abc]-', line)
    if match:
        print(line)
print('=========================')

for line in strings:
    match = re.search(r'-[abc]+-', line)
    if match:
        print(line)
print('=========================')

for line in strings:
    match = re.search(r'-[abc]*-', line)
    if match:
        print(line)


