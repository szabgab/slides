from collections import deque

fruits = deque()

print(type(fruits))  # <type 'collections.deque'>
print(fruits)        # deque([])
print(len(fruits))   # 0

fruits.append('Apple')
print(fruits)        # deque(['Apple'])
print(len(fruits))   # 1

fruits.append('Banana')
fruits.append('Peach')
print(fruits)        # deque(['Apple', 'Banane', 'Peach'])
print(len(fruits))   # 3

nxt = fruits.popleft()
print(nxt)           # 'Apple'
print(fruits)        # deque(['Banana', 'Peach'])
print(len(fruits))   # 2

if fruits:
    print("The queue has items")
else:
    print("The queue is empty")

nxt = fruits.popleft()
nxt = fruits.popleft()

if fruits:
    print("The queue has items")
else:
    print("The queue is empty")


