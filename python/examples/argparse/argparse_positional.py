import argparse

parser = argparse.ArgumentParser()
parser.add_argument('name', help='your full name')
args = parser.parse_args()

print(args.name)
