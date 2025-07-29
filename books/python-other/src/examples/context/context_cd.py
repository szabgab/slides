import sys
import os
from mycwd import cwd

def do_something(path):
    with cwd(path):
        content = os.listdir()
        if len(content) < 10:
            return

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} PATH")
    path = sys.argv[1]
    print(os.getcwd())
    do_something(path)
    print(os.getcwd())

main()
