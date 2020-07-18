import sys
import string
import random
import argparse
import os

# Generate n file of size S with random letters

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',             help="Directory where to create the files", default=".")
    parser.add_argument('--files', type=int, help="Number of files to create", default=1)
    parser.add_argument('--size',  type=int, help="Size of files",             default=10)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    chars = list(string.ascii_lowercase) + [' '] * 5 + ['\n']

    for ix in range(args.files):
        all_chars = []
        for _ in range(args.size):
            all_chars.extend(random.sample(chars, 1))
        #print(len(all_chars))

        #print(all_chars)
        filename = os.path.join(args.dir, str(ix) + '.txt')
        with open(filename, 'w') as fh:
            fh.write(''.join(all_chars))


def old_main():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} NUMBER_OF_ROWS")

    row_count = int(sys.argv[1])
    min_width = 30
    max_width = 50
    filename  = 'data.log'

    chars = list(string.ascii_lowercase) + [' '] * 5
    all_chars = chars * max_width

    with open(filename, 'w') as fh:
        for i in range(row_count):
            width = random.randrange(min_width, max_width+1)
            row = ''.join(random.sample(all_chars, width))
            fh.write(row + "\n")

main()
