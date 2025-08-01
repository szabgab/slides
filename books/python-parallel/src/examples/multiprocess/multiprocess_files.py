import multiprocessing as mp
import os
import sys

def analyze(filename):
    print("Process {:>5} analyzing {}".format(os.getpid(), filename))
    digits = 0
    letters = 0
    spaces = 0
    other = 0
    total  = 0
    with open(filename) as fh:
        for line in fh:
            for char in line:
                total += 1
                if char.isdigit():
                    digits += 1
                    break
                if char.isalnum():
                    letters += 1
                    break
                if char == ' ':
                    spaces += 1
                    break
                other += 1
    return {
        'filename': filename,
        'total': total,
        'digits': digits,
        'spaces': spaces,
        'letters': letters,
        'other': other,
    }

def main():
    if len(sys.argv) < 3:
        exit(f"Usage: {sys.argv[0]} POOL_SIZE FILEs")
    size  = int(sys.argv[1])
    files = sys.argv[2:]

    with mp.Pool(size) as pool:
        results = pool.map(analyze, files)
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
