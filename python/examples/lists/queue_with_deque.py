from collections import deque

# items = deque([])
items = deque(['foo', 'bar'])

print(type(items))  # <type 'collections.deque'>
print(items)        # deque(['foo', 'bar'])

items.append('zorg')
print(items)        # deque(['foo', 'bar', 'zorg'])
print(len(items))   # 3

items.append('zorg')
print(items)        # deque(['foo', 'bar', 'zorg', 'zorg'])

nxt = items.popleft()
print(nxt)          # 'foo'
print(items)        # deque(['bar', 'zorg', 'zorg'])

print(len(items))   # 3

if items:
    print("The queue has items")
else:
    print("The queue is empty")
