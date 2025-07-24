stack = []

print("x = eXit, s = Show, [+-*/=]")
while True:
    val = input(':')

    if val == 's':
        print(stack)
        continue

    if val == 'x':
        break

    if val == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
        continue

    if val == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a-b)
        continue

    if val == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
        continue

    if val == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a/b)
        continue

    if val == '=':
        print(stack.pop())
        continue

    stack.append(float(val))
