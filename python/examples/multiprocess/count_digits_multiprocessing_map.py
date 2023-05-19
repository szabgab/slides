import sys
import count_digits
import multiprocessing as mp

def main():
    if len(sys.argv) < 3:
        exit(f"Usage: {sys.argv[0]} POOL FILENAMEs")

    size = int(sys.argv[1])
    files = sys.argv[2:]

    with mp.Pool(size) as pool:
        results = pool.map(count_digits.count_digits, files)
    count_digits.print_table(list(results))

if __name__ == "__main__":
    main()

