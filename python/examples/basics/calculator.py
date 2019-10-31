
def main():
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
        return

    print(res)
    return


main()

