import sys

table = {
    "+" : lambda x, y: x+y,
    "-" : lambda x, y: x-y,
    "*" : lambda x, y: x*y,
    "/" : lambda x, y: x/y,
}


def main():
    if len(sys.argv) != 4:
        exit(f"Usage: {sys.argv[0]} NUMBER OP NUMBER")
    action = table[sys.argv[2]]
    print( action(int(sys.argv[1]), int(sys.argv[3])) )

main()


