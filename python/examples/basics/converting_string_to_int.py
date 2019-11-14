a = "42 for life"
print(a)                # 42 for life
print( type(a) )        # <class 'str'>

b = int(a)
print(b)
print( type(b) )

# Traceback (most recent call last):
#   File "converting_string_to_int.py", line 5, in <module>
#     b = int(a)
# ValueError: invalid literal for int() with base 10: '42 for life'
