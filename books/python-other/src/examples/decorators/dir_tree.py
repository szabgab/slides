import sys
import os

def traverse(path):
    if os.path.isfile(path):
        print(path)
        return
    if os.path.isdir(path):
        for item in os.listdir(path):
            traverse(os.path.join(path, item))
        return
    # other unhandled things


if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} DIR|FILE")
traverse(sys.argv[1])


