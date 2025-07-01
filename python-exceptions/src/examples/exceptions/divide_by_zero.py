def div(a, b):
    print("before")
    print(a/b)
    print("after")

div(1, 0)

# before
# Traceback (most recent call last):
#   File "examples/exceptions/divide_by_zero.py", line 6, in <module>
#     div(1, 0)
#   File "examples/exceptions/divide_by_zero.py", line 3, in div
#     print(a/b)
#           ~^~
# ZeroDivisionError: division by zero

