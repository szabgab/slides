a = float(input("Number: "))
b = float(input("Number: "))
op = input("Operator (+-*/): ")

if op == '+':
    res = a+b
elif op == '-':
    res = a-b
elif op == '*':
    res = a*b
elif op == '/':
    res = a/b
else:
    print("Invalid operator: '{}'".format(op))
    exit()


print(res)


