import sys
import os

def do_something(path):
    start_dir = os.getcwd()
    os.chdir(path)

    content = os.listdir()
    number = len(content)
    print(number)
    if number < 15:
        return

    os.chdir(start_dir)

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} PATH")
    path = sys.argv[1]
    print(os.getcwd())
    do_something(path)
    print(os.getcwd())

main()
