import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--fname')     # optional named parameter that requires a value
parser.add_argument('--lname',   help="Some description")

parser.add_argument('--max',     help='max number of somthing', type=int) # check and convert to integer
parser.add_argument('--verbose', action='store_true') # "flag" no value is expected

parser.add_argument('--color', '-c') # short name also accepted


#parser.add_argument('files',  help="filenames(s)")   # a required positional argument
#parser.add_argument('dirs',   nargs="*")   # 0 or more positional
#parser.add_argument('places', nargs="+")   # 1 or more positional
#parser.add_argument('ords', nargs="?")   # 0 or 1 positional

parser.add_argument('--things', nargs="+")  # --things a.txt b.txt c.txt


args = parser.parse_args()

print(f"fname:   {args.fname}")
print(f"verbose: {args.verbose}")
print(f"things:  {args.things}")
print(f"color:   {args.color}")
print(f"max:     {args.max}")

if args.verbose:
    print("we are making progress....")

