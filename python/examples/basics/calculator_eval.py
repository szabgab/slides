
def main():
    a = input("Number: ")
    b = input("Number: ")
    op = input("Operator (+-*/): ")

    command = a + op + b
    print(command)
    res = eval(command)
    print(res)

main()
