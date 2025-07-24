lines = [
    'abc def ghi',
    'hello world',
]

collector = []

for l in lines:
   collector.extend(l.split())
   print(collector)

# ['abc', 'def', 'ghi']
# ['abc', 'def', 'ghi', 'hello', 'world']

