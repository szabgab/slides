import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output',   help="Some description")

args = parser.parse_args()

print(f"input:   {args.input}")
print(f"output: {args.output}")


