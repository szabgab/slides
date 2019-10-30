import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')     # optional named parameter that requires a value
parser.add_argument('--name', help="Some description")

parser.add_argument('--max', help='max number of somthing', type=int) # check and convert to integer
parser.add_argument('--verbose', action='store_true') # "flag" no value is expected

parser.add_argument('--color', '-c') # short name also accepted


parser.add_argument('files', help="filenames(s)")   # a required positional argument
parser.add_argument('files', nargs="*")   # 0 or more positional
parser.add_argument('files', nargs="+")   # 1 or more positional

args = parser.parse_args()

print(args.name)
print(args.files)

