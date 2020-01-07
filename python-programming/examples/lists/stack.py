stack = []

stack.append("Joe")
print(stack)
stack.append("Jane")
print(stack)
stack.append("Bob")
print(stack)

while stack:
    name = stack.pop()
    print(name)
    print(stack)
