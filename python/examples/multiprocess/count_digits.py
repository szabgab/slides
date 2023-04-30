import sys
import string

def count_digits(filename):
    count = {}
    for cr in string.digits:
        count[cr] = 0
    with open(filename) as fh:
        for row in fh:
            for cr in row:
                if cr in string.digits:
                    count[cr] += 1

    return {
        "filename": filename,
        "count": count,
    }


def print_table(results):
    dw = 6
    width = 0
    for res in results:
        width = max(width, len(res["filename"]))

    print(" " * (width + 1), end="")
    for n in range(10):
        print(f"{n:{dw}}", end="")
    print("")

    for res in results:
        print(f'{res["filename"]:{width}} ', end="")
        for digit in string.digits:
            print(f"{res['count'][digit]:{dw}}", end="")
        print("")

    total = {}
    for digit in string.digits:
        total[digit] = 0
    for res in results:
        for digit in string.digits:
            total[digit] += res["count"][digit]

    name = "TOTAL"
    print(f'{name:{width}} ', end="")
    for digit in string.digits:
        print(f"{total[digit]:{dw}}", end="")
    print("")


def main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAMEs")

    files = sys.argv[1:]
    results = []
    for filename in files:
        result = count_digits(filename)
        results.append(result)
    print_table(results)


if __name__ == "__main__":
    main()

