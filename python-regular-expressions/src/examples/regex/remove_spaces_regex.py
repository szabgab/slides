import re

line = "  ab cd  "

res = re.sub(r'^\s+', '', line)  # leading
print(f"'{res}'")

res = re.sub(r'\s+$', '', line)  # trailing
print(f"'{res}'")


