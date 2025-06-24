import re

txt = 'text with slash \ and more text'
print(txt)         # text with slash \ and more text

# m0 = re.search('\', txt)
    # SyntaxError: EOL while scanning string literal

# m0 = re.search('\\', txt)
    # Exception:  sre_constants.error: bogus escape (end of line)
    # because the regex engine does not know what to do with a single \

m1 = re.search('\\\\', txt)
if m1:
    print('m1')    # m1

m2 = re.search(r'\\', txt)
if m2:
    print('m2')    # m2
