import re

text = """
text with cat in the middle
cat with dog
dog with cat"""

if re.search(r'dog', text):
    print(text)

print("---")
if re.search(r'^dog', text):
    print('Carret dog')

print("---")
if re.search(r'\Adog', text):
    print('A dog')

print("---")
if re.search(r'dog$', text):
    print('$ dog')

print("---")
if re.search(r'dog\Z', text):
    print('Z dog')

print("-----------------")
if re.search(r'^dog', text, re.MULTILINE):
    print('^ dog')

print("---")
if re.search(r'\Adog', text, re.MULTILINE):
    print('A dog')

print("---")
if re.search(r'dog$', text, re.MULTILINE):
    print('$ dog')

print("---")
if re.search(r'dog\Z', text, re.MULTILINE):
    print('Z dog')

