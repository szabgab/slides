import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} short-STRING long-STRING")

string = sys.argv[1]
text   = sys.argv[2]

if string in text:
    loc = text.index(string)
    print(string, "can be found in ", text, "at", loc)
else:
    print(string, "can NOT be found in ", text)

