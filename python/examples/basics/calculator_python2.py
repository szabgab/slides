from __future__ import print_function

a = float(raw_input("Number: "))
b = float(raw_input("Number: "))
op = raw_input("Operator (+-*/): ")

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


