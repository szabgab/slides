# file_a = "c:\Users\Foobar\readme.txt"
# print(file_a)

# Python2:  eadme.txtFoobar
# Python3:
#   File "examples/strings/raw.py", line 6
#     file_a = "c:\Users\Foobar\readme.txt"
#             ^
# SyntaxError: (unicode error) 'unicodeescape' codec
#    can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


file_b = "c:\\Users\\Foobar\\readme.txt"
print(file_b)  # c:\Users\Foobar\readme.txt

file_c = r"c:\Users\Foobar\readme.txt"
print(file_c)  # c:\Users\Foobar\readme.txt

text = r"text \n \d \s \ and more"
print(text)    # text \n \d \s \ and more
