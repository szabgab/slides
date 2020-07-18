import re

strings = (
    "axxxa",
    "axxxxa",
    "axxxxxa",
)

for text in strings:
    match = re.search(r'ax{4}', text)
    if match:
        print("Match")
        print(match.group(0))
    else:
        print("NOT Match")
