import re

match = re.search(r'a.*b', 'axbzb')
print(match.group(0))

match = re.search(r'a.*?b', 'axbzb')
print(match.group(0))


match = re.search(r'a.*b', 'axy121413413bq')
print(match.group(0))

match = re.search(r'a.*?b', 'axyb121413413q')
print(match.group(0))
