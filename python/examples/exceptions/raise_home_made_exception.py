class MyException(Exception):
    def __init__(self, first, second):
        self.first  = first
        self.second = second
    def __str__(self):
        return 'Problems? {} and {}'.format(self.first, self.second)


def some():
    print("Entering some function")
    raise MyException("Some", "Error")
    print("Code after raise")

try:
    print("Before calling some")
    some()
    print("After calling some")
except Exception as e:
    print("Exception received")
    print(e)
    print("Type: " + type(e).__name__)

# Before calling some
# Entering some function
# Exception received
# Problems? Some and Error
# Type: MyException
