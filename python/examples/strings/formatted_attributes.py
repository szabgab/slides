import sys

txt = "Some text"
num = 42.12

print("{1.executable}, {0}".format(txt, sys))
    #  /usr/local/opt/python/bin/python2.7, Some text
print("{system.argv[0]}, {text}".format(
    text = txt, system = sys)) #  formatted_indexing.py, Some text
