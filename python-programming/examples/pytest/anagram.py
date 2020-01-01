from mymod_1 import is_anagram
import sys

if len(sys.argv) != 3:
    exit("Usage {} STR STR".format(sys.argv[0]))

print(is_anagram(sys.argv[1], sys.argv[2]))

