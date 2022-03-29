import re

text = "שלום כיתה א"
print(text)


match = re.search(r"[א-ת]", text)
print(match.group(0))  # ש

match = re.search(r"[א-ת]*", text)
print(match.group(0))  # שלום

match = re.search(r"[ א-ת]*", text)
print(match.group(0))  # שלום כיתה א

