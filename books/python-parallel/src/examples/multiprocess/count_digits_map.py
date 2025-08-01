import sys
import count_digits

def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAMEs")

    files = sys.argv[1:]
    results = map(count_digits.count_digits, files)
    count_digits.print_table(list(results))

if __name__ == "__main__":
    main()

