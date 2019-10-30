from __future__ import print_function

a = raw_input("Number: ")
b = raw_input("Number: ")
op = raw_input("Operator (+-*/): ")

command = a + op + b
print(command)
res = eval(command)
print(res)

