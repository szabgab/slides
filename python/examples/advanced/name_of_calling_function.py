import inspect

def first():
    print("in first")
    print("Called by", inspect.stack()[1][3])
    second()

def second():
    print("in second")
    print("Called by", inspect.stack()[1][3])

def main():
    first()

main()

