import sys
import os

def walker(path, todo):
    if os.path.isdir(path):
        items = os.listdir(path)
        for item in items:
            walker(os.path.join(path, item), todo)
    else:
        todo(path)


def print_size(name):
    print(f"{os.stat(name).st_size:6}  {name} ")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} PATH")
    walker(sys.argv[1], print)
    #walker(sys.argv[1], print_size)
    #walker(sys.argv[1], lambda name: print(f"{os.stat(name).st_size:6}  {name[::-1]} "))

