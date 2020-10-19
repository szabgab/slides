import sys
import codecs

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} TEXT")

original = sys.argv[1]

encoded = ''
for char in original:
    code = ord(char)
    if 97 <= code and code <= 122:
        new_char = chr((code-97 + 13 ) % 26 + 97)
    elif 65 <= code and code <= 90:
        new_char = chr((code-65 + 13 ) % 26 + 65)
    else:
        new_char = char

    encoded += new_char

print(encoded)

