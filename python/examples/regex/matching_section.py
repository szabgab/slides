import re

text = "This is <a string> with some sections <marked> with special characters"

m = re.search(r'<.*>', text)
if m:
    print(m.group(0))
