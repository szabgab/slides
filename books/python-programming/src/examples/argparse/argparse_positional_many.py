import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', help='filename(s)', nargs='+')
args = parser.parse_args()

print(args.files)

