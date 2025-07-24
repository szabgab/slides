import sys

def main():
    if len(sys.argv) != 2:
        exit("Usage: " + sys.argv[0] + " VALUE")
    print("Hello " + sys.argv[1])

main()
