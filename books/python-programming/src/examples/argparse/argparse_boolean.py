import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--color',   help='The name of the color')
parser.add_argument('--verbose', help='Print more data',
    action='store_true')
args = parser.parse_args()

print(args.color)
print(args.verbose)

