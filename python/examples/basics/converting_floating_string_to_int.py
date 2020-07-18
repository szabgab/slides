a = "2.1"
print(a)          # 2.1
print( type(a) )  # <class 'str'>

b = int(a)
print(b) 
print( type(b) )

# Traceback (most recent call last):
#   File "converting_floating_string_to_int.py", line 5, in <module>
#     b = int(a)
# ValueError: invalid literal for int() with base 10: '2.1'
