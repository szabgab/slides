def some():
    print("Entering some function")
    raise Exception("Some Error")
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
# Some Error
# Type: Exception
