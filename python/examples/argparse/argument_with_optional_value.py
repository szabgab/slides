import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--level',     help='Some level', type=int, const=10, nargs='?')
args = parser.parse_args()

print(args.level)
