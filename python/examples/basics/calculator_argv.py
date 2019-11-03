import sys


def main():
    if len(sys.argv) < 4:
        exit("Usage: " + sys.argv[0] + " OPERAND OPERATOR OPERAND")

    a = float(sys.argv[1])
    b = float(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a / b
    else:
        print("Invalid operator: '{}'".format(op))
        exit()

    print(res)

main()
