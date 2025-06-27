import sys

def main():
    if len(sys.argv) != 4:
        exit(f"Usage: {sys.argv[0]} NUMBER OPERATOR NUMBER")

    command = sys.argv[1] + sys.argv[2] + sys.argv[3]
    print(command)
    res = eval(command)
    print(res)

main()
