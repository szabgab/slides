import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} TEXT")

original = sys.argv[1]

encoded = ''
for char in original:
    code = ord(char)
    if 'a' <= char <= 'z':
    #if ord('a') <= code and code <= ord('z'):
        new_char = chr((code-ord('a') + 13 ) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        new_char = chr((code-65 + 13 ) % 26 + 65)
    else:
        new_char = char

    encoded += new_char

print(encoded)

