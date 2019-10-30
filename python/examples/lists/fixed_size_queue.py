from collections import deque

queue = deque([], maxlen = 3)
print(len(queue))     # 0
print(queue.maxlen)   # 3

queue.append("Foo")
queue.append("Bar")
queue.append("Baz")
print(queue)          # deque(['Foo', 'Bar', 'Baz'], maxlen=3)

queue.append("Zorg")  # Automatically removes the left-most (first) element
print(queue)          # deque(['Bar', 'Baz', 'Zorg'], maxlen=3)

