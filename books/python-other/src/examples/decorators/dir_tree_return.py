import sys
import os

def traverse(path, func):
    response = {}
    if os.path.isfile(path):
        func(path)
        return response
    if os.path.isdir(path):
        for item in os.listdir(path):
            traverse(os.path.join(path, item), func)
        return response
    # other unhandled things


if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} DIR|FILE")
#traverse(sys.argv[1], print)
#traverse(sys.argv[1], lambda path: print(f"{os.path.getsize(path):>6} {path}"))


