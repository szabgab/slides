import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--color', help='The name of the color')
args = parser.parse_args()

print(args.color)
