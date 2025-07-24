import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--age', help='Your age in years', type=float, required=True)
args = parser.parse_args()

if args.age < 0:
    parser.print_help()
    exit(1)

print(args.age)
