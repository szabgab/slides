from ctypes import cdll
from ctypes import c_char_p

hello_lib = cdll.LoadLibrary("hello.so")

print(hello_lib.add_int(4, 5))         # 9

print(hello_lib.echo('Hello World'))   # 153977204


hello_lib.echo.restype = c_char_p
print(hello_lib.echo('Hello World'))   # Hello World



