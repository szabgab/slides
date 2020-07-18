from collections import deque
stack = deque()

stack.append("Joe")
stack.append("Jane")
stack.append("Bob")

while stack:
    name = stack.pop()
    print(name)

# Bob
# Jane
# Joe

