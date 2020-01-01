from multiprocessing import Pool
import os
import sys
import re

def analyze(filename):
    print("Process {:>5} analyzing {}".format(os.getpid(), filename))
    digits = 0
    spaces = 0
    total  = 0
    with open(filename) as fh:
        for line in fh:
            for char in line:
                total += 1
                if re.search(r'^\d$', char):
                   digits += 1
                if char == ' ':
                   spaces += 1
    return {
        'filename': filename,
        'total': total,
        'digits': digits,
        'spaces': spaces,
    }

def main():
    if len(sys.argv) < 3:
        exit("Usage: {} POOL_SIZE FILEs")
    size  = int(sys.argv[1])
    files = sys.argv[2:]

    with Pool(size) as p:
        results = p.map(analyze, files)
    for res in results:
        print(res)

if __name__ == '__main__':
    main()
