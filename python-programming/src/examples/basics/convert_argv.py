import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} INPUT_FILE OUTPUT_FILE")

input_file = sys.argv[1]
output_file = sys.argv[2]

print(f"This code will read {input_file}, analyze it and then create {output_file}")
...
