from ctypes import cdll
from ctypes import c_char_p

more_lib = cdll.LoadLibrary("more.so")

print(more_lib.len("abcd"))      # 4
print(more_lib.len(""))          # 0
print(more_lib.len("x" * 123))   # 123


more_lib.concat.restype = c_char_p
print(more_lib.concat("abc", "def"))

