import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " VALUE")
        exit(3)
    print("Hello " + sys.argv[1])

main()
