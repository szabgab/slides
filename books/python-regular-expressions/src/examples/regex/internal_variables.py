import re


line = "one 123 and two 123 and oxxo 23"

match = re.search(r"(.)(.)\2\1", line)
if match:
    print(match.group(1)) # o
    print(match.group(2)) # x

match = re.search(r"(\d\d).*\1", line)
if match:
    print(match.group(1)) # 12

match = re.search(r"(\d\d).*\1.*\1", line)
if match:
    print(match.group(1)) # 23


match = re.search(r"(\d\d).*\1{2,3}",  "45 afjh 4545 kjdhfkh")
if match:
    print(match.group(1)) # 45


# (.{5}).*\1

