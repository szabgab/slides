text = "abcd"
print(text)     # abcd

text[2] = 'Y'

# abcd
# Traceback (most recent call last):
#   File "examples/strings/string_change.py", line 6, in <module>
#     text[2] = 'Y'
# TypeError: 'str' object does not support item assignment
