import inspect

def first():
    print(inspect.currentframe().f_code.co_name)
    print(inspect.stack()[0][3])
    second()


def second():
    print(inspect.currentframe().f_code.co_name)
    print(inspect.stack()[0][3])

def main():
    first()

main()
