class MyException(Exception):
    pass

def some():
    raise MyException("Some Error")

def main():
    try:
        some()
    except Exception as err:
        print(err)
        print("Type: " + type(err).__name__)


    try:
        some()
    except MyException as err:
        print(err)

main()
