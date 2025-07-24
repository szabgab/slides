import sys
import codecs

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} TEXT")

original = sys.argv[1]

encoded = codecs.encode(original, encoding='rot_13')

print(encoded)
